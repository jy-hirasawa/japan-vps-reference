"""
tests/test_check_links.py — scripts/check_links.py の単体テスト
"""

import io
import sys
import tempfile
import unittest
import http.client
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_links


class TestCheckLinksHelpers(unittest.TestCase):

    def test_request_status_returns_status_on_success(self):
        class DummyResponse:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                return False

            def getcode(self):
                return 204

        with patch("check_links.request.urlopen", return_value=DummyResponse()):
            self.assertEqual(
                check_links.request_status("https://example.com/ok", method="HEAD"),
                (204, None),
            )

    def test_request_status_returns_status_on_http_error(self):
        http_error = check_links.error.HTTPError(
            url="https://example.com/missing",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )
        with patch("check_links.request.urlopen", side_effect=http_error):
            self.assertEqual(
                check_links.request_status("https://example.com/missing", method="HEAD"),
                (404, None),
            )

    def test_request_status_handles_http_exception_as_temporary_error(self):
        with patch(
            "check_links.request.urlopen",
            side_effect=http.client.IncompleteRead(b"partial", 10),
        ):
            status, reason = check_links.request_status("https://example.com/broken", method="HEAD")

        self.assertIsNone(status)
        self.assertIn("IncompleteRead", reason)

    def test_is_check_target_url(self):
        self.assertTrue(check_links.is_check_target_url("https://example.com/path"))
        self.assertTrue(check_links.is_check_target_url("http://example.com/path"))
        self.assertFalse(check_links.is_check_target_url("unknown"))
        self.assertFalse(check_links.is_check_target_url(""))
        self.assertFalse(check_links.is_check_target_url("example.com/path"))

    def test_iter_official_urls_keeps_key_and_skips_invalid_values(self):
        data = {
            "providers": [
                {
                    "id": "alpha",
                    "official_urls": {
                        "top": {"url": "https://example.com/top"},
                        "support": {"url": "unknown"},
                        "terms": {"url": ""},
                        "pricing": {"url": "not-a-url"},
                    },
                }
            ]
        }

        self.assertEqual(
            check_links.iter_official_urls(data),
            [
                {
                    "source": "providers",
                    "provider_id": "alpha",
                    "official_url_key": "top",
                    "url": "https://example.com/top",
                }
            ],
        )

    def test_iter_evidence_urls_keeps_feature_id_and_skips_invalid_values(self):
        data = {
            "evidence": [
                {
                    "provider_id": "alpha",
                    "feature_id": "api",
                    "source_url": "https://example.com/api",
                },
                {
                    "provider_id": "alpha",
                    "feature_id": "cli",
                    "source_url": "unknown",
                },
                {
                    "provider_id": "alpha",
                    "feature_id": "docs",
                    "source_url": "not-a-url",
                },
            ]
        }

        self.assertEqual(
            check_links.iter_evidence_urls(data),
            [
                {
                    "source": "evidence",
                    "provider_id": "alpha",
                    "feature_id": "api",
                    "url": "https://example.com/api",
                }
            ],
        )

    def test_collect_targets_deduplicates_same_url(self):
        providers_data = {
            "providers": [
                {
                    "id": "alpha",
                    "official_urls": {
                        "top": {"url": "https://example.com/shared"},
                        "pricing": {"url": "https://example.com/pricing"},
                    },
                }
            ]
        }
        evidence_data = {
            "evidence": [
                {
                    "provider_id": "alpha",
                    "feature_id": "api",
                    "source_url": "https://example.com/shared",
                },
                {
                    "provider_id": "alpha",
                    "feature_id": "pricing",
                    "source_url": "https://example.com/pricing",
                },
            ]
        }

        targets = check_links.collect_targets(providers_data, evidence_data)

        self.assertEqual(set(targets), {"https://example.com/shared", "https://example.com/pricing"})
        self.assertEqual(len(targets["https://example.com/shared"]), 2)
        self.assertEqual(len(targets["https://example.com/pricing"]), 2)

    def test_check_url_distinguishes_broken_and_temporary_failures(self):
        with patch.object(check_links, "request_status", return_value=(404, None)):
            self.assertEqual(
                check_links.check_url("https://example.com/missing"),
                (False, "kind=broken status=404"),
            )

        with patch.object(check_links, "request_status", return_value=(429, None)):
            self.assertEqual(
                check_links.check_url("https://example.com/limited"),
                (False, "kind=temporary status=429"),
            )

        with patch.object(check_links, "request_status", return_value=(None, "timed out")):
            self.assertEqual(
                check_links.check_url("https://example.com/timeout"),
                (False, "kind=temporary error=timed out"),
            )

        with patch.object(check_links, "request_status", return_value=(503, None)):
            self.assertEqual(
                check_links.check_url("https://example.com/unavailable"),
                (False, "kind=temporary status=503"),
            )

        with patch.object(check_links, "request_status", return_value=(200, None)):
            self.assertEqual(
                check_links.check_url("https://example.com/ok"),
                (True, "status=200"),
            )

    def test_check_url_falls_back_to_get_for_head_specific_failures(self):
        for status in (400, 403, 405):
            with self.subTest(status=status):
                with patch.object(
                    check_links,
                    "request_status",
                    side_effect=[(status, None), (200, None)],
                ) as mock_request_status:
                    self.assertEqual(
                        check_links.check_url("https://example.com/fallback"),
                        (True, "status=200"),
                    )

                self.assertEqual(mock_request_status.call_count, 2)
                self.assertEqual(mock_request_status.call_args_list[0].kwargs["method"], "HEAD")
                self.assertEqual(mock_request_status.call_args_list[1].kwargs["method"], "GET")


class TestCheckLinksMain(unittest.TestCase):

    def test_main_checks_each_unique_url_once_and_reports_references(self):
        providers_data = {
            "providers": [
                {
                    "id": "alpha",
                    "official_urls": {
                        "top": {"url": "https://example.com/shared"},
                        "pricing": {"url": "https://example.com/missing"},
                    },
                }
            ]
        }
        evidence_data = {
            "evidence": [
                {
                    "provider_id": "alpha",
                    "feature_id": "api",
                    "source_url": "https://example.com/shared",
                },
                {
                    "provider_id": "alpha",
                    "feature_id": "cli",
                    "source_url": "https://example.com/missing",
                },
            ]
        }

        checked_urls: list[str] = []

        def fake_check_url(url: str) -> tuple[bool, str]:
            checked_urls.append(url)
            if url.endswith("/missing"):
                return False, "kind=broken status=404"
            return True, "status=200"

        with tempfile.TemporaryDirectory() as tmpdir:
            providers_path = Path(tmpdir) / "providers.yml"
            evidence_path = Path(tmpdir) / "evidence.yml"
            providers_path.write_text("providers: []\n", encoding="utf-8")
            evidence_path.write_text("evidence: []\n", encoding="utf-8")

            stdout = io.StringIO()
            stderr = io.StringIO()
            with (
                patch.object(check_links, "PROVIDERS_YML", providers_path),
                patch.object(check_links, "EVIDENCE_YML", evidence_path),
                patch.object(check_links, "load_yaml", side_effect=[providers_data, evidence_data]),
                patch.object(check_links, "check_url", side_effect=fake_check_url),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                exit_code = check_links.main()

        self.assertEqual(exit_code, 1)
        self.assertEqual(
            checked_urls,
            ["https://example.com/shared", "https://example.com/missing"],
        )
        self.assertIn("[OK] url=https://example.com/shared status=200", stdout.getvalue())
        stderr_text = stderr.getvalue()
        self.assertIn("[FAIL] url=https://example.com/missing kind=broken status=404", stderr_text)
        self.assertIn("  - providers: alpha / pricing", stderr_text)
        self.assertIn("  - evidence: alpha / cli", stderr_text)


if __name__ == "__main__":
    unittest.main()
