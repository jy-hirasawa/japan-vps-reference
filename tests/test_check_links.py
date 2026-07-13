"""
tests/test_check_links.py — scripts/check_links.py の単体テスト
"""

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_links


class TestCheckLinksHelpers(unittest.TestCase):

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
