#!/usr/bin/env python3
"""
check_links.py — providers.yml / evidence.yml の URL リンク状態を確認するスクリプト

使い方:
    python scripts/check_links.py
"""

import http.client
import socket
import sys
from collections import defaultdict
from pathlib import Path
from urllib import error, request
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROVIDERS_YML = ROOT / "providers.yml"
EVIDENCE_YML = ROOT / "evidence.yml"
TIMEOUT_SECONDS = 10
USER_AGENT = "japan-vps-reference-link-check/1.0"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def is_check_target_url(value: str) -> bool:
    url = value.strip()
    if not url or url == "unknown":
        return False

    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def iter_official_urls(data: dict) -> list[dict[str, str]]:
    providers = data.get("providers", [])
    if not isinstance(providers, list):
        raise ValueError("providers.yml: 'providers' キーがリストではありません。")

    urls: list[dict[str, str]] = []
    for provider in providers:
        provider_id = str(provider.get("id", "?"))
        official_urls = provider.get("official_urls", {})
        if not isinstance(official_urls, dict):
            continue

        for key, entry in official_urls.items():
            if not isinstance(entry, dict):
                continue
            url = str(entry.get("url", "")).strip()
            if not is_check_target_url(url):
                continue
            urls.append(
                {
                    "source": "providers",
                    "provider_id": provider_id,
                    "official_url_key": str(key),
                    "url": url,
                }
            )
    return urls


def iter_evidence_urls(data: dict) -> list[dict[str, str]]:
    evidence = data.get("evidence", [])
    if not isinstance(evidence, list):
        raise ValueError("evidence.yml: 'evidence' キーがリストではありません。")

    urls: list[dict[str, str]] = []
    for entry in evidence:
        if not isinstance(entry, dict):
            continue

        url = str(entry.get("source_url", "")).strip()
        if not is_check_target_url(url):
            continue

        urls.append(
            {
                "source": "evidence",
                "provider_id": str(entry.get("provider_id", "?")),
                "feature_id": str(entry.get("feature_id", "?")),
                "url": url,
            }
        )
    return urls


def collect_targets(providers_data: dict, evidence_data: dict) -> dict[str, list[dict[str, str]]]:
    targets: dict[str, list[dict[str, str]]] = defaultdict(list)
    for ref in iter_official_urls(providers_data):
        targets[ref["url"]].append(ref)
    for ref in iter_evidence_urls(evidence_data):
        targets[ref["url"]].append(ref)
    return dict(targets)


def request_status(url: str, method: str) -> tuple[int | None, str | None]:
    req = request.Request(url=url, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            return resp.getcode(), None
    except error.HTTPError as exc:
        return exc.code, None
    except (error.URLError, TimeoutError, socket.timeout, http.client.HTTPException) as exc:
        reason = getattr(exc, "reason", exc)
        return None, str(reason)


def check_url(url: str) -> tuple[bool, str]:
    status, reason = request_status(url, method="HEAD")
    if status in {400, 403, 405}:
        status, reason = request_status(url, method="GET")

    if status is None:
        return False, f"kind=temporary error={reason}"
    if 200 <= status < 400:
        return True, f"status={status}"
    if status in {403, 429} or status >= 500:
        return False, f"kind=temporary status={status}"
    return False, f"kind=broken status={status}"


def format_failure(url: str, detail: str, refs: list[dict[str, str]]) -> str:
    lines = [f"[FAIL] url={url} {detail}"]
    for ref in refs:
        if ref["source"] == "providers":
            lines.append(f"  - providers: {ref['provider_id']} / {ref['official_url_key']}")
            continue
        lines.append(f"  - evidence: {ref['provider_id']} / {ref['feature_id']}")
    return "\n".join(lines)


def main() -> int:
    if not PROVIDERS_YML.exists():
        print(f"[ERROR] ファイルが見つかりません: {PROVIDERS_YML}", file=sys.stderr, flush=True)
        return 1
    if not EVIDENCE_YML.exists():
        print(f"[ERROR] ファイルが見つかりません: {EVIDENCE_YML}", file=sys.stderr, flush=True)
        return 1

    providers_data = load_yaml(PROVIDERS_YML)
    evidence_data = load_yaml(EVIDENCE_YML)
    try:
        targets = collect_targets(providers_data, evidence_data)
    except ValueError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr, flush=True)
        return 1

    if not targets:
        print("チェック対象の official_urls / source_url はありません。", flush=True)
        return 0

    failures = 0
    for url, refs in targets.items():
        ok, detail = check_url(url)
        if ok:
            print(f"[OK] url={url} {detail}", flush=True)
            continue
        failures += 1
        print(format_failure(url, detail, refs), file=sys.stderr, flush=True)

    if failures:
        print(f"\nリンクチェック失敗: {failures} 件", file=sys.stderr, flush=True)
        return 1

    print(f"\nリンクチェック成功: {len(targets)} 件", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
