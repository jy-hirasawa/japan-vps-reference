#!/usr/bin/env python3
"""
check_links.py — providers.yml の official_urls リンク状態を確認するスクリプト

使い方:
    python scripts/check_links.py
"""

import socket
import sys
from pathlib import Path
from urllib import error, request

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROVIDERS_YML = ROOT / "providers.yml"
TIMEOUT_SECONDS = 10
USER_AGENT = "japan-vps-reference-link-check/1.0"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def iter_official_urls(data: dict) -> list[tuple[str, str]]:
    providers = data.get("providers", [])
    if not isinstance(providers, list):
        raise ValueError("providers.yml: 'providers' キーがリストではありません。")

    urls: list[tuple[str, str]] = []
    for provider in providers:
        provider_id = str(provider.get("id", "?"))
        official_urls = provider.get("official_urls", {})
        if not isinstance(official_urls, dict):
            continue

        for entry in official_urls.values():
            if not isinstance(entry, dict):
                continue
            url = str(entry.get("url", "")).strip()
            if not url or url == "unknown":
                continue
            urls.append((provider_id, url))
    return urls


def request_status(url: str, method: str) -> tuple[int | None, str | None]:
    req = request.Request(url=url, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            return resp.getcode(), None
    except error.HTTPError as exc:
        return exc.code, None
    except (error.URLError, TimeoutError, socket.timeout) as exc:
        reason = getattr(exc, "reason", exc)
        return None, str(reason)


def check_url(url: str) -> tuple[bool, str]:
    status, reason = request_status(url, method="HEAD")
    if status == 405:
        status, reason = request_status(url, method="GET")

    if status is None:
        return False, f"request error: {reason}"
    if 200 <= status < 400:
        return True, f"status={status}"
    return False, f"status={status}"


def main() -> int:
    if not PROVIDERS_YML.exists():
        print(f"[ERROR] ファイルが見つかりません: {PROVIDERS_YML}", file=sys.stderr)
        return 1

    data = load_yaml(PROVIDERS_YML)
    try:
        targets = iter_official_urls(data)
    except ValueError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    if not targets:
        print("チェック対象の official_urls はありません。")
        return 0

    failures: list[tuple[str, str, str]] = []
    for provider_id, url in targets:
        ok, detail = check_url(url)
        if ok:
            print(f"[OK] provider_id={provider_id} url={url} ({detail})")
            continue
        failures.append((provider_id, url, detail))
        print(f"[FAIL] provider_id={provider_id} url={url} ({detail})", file=sys.stderr)

    if failures:
        print(f"\nリンクチェック失敗: {len(failures)} 件", file=sys.stderr)
        return 1

    print(f"\nリンクチェック成功: {len(targets)} 件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
