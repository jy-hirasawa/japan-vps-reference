#!/usr/bin/env python3
"""
validate.py — providers.yml / features.yml / evidence.yml / benchmarks.yml の必須フィールド検証スクリプト

使い方:
    python scripts/validate.py
"""

import re
import sys
import yaml
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PROVIDER_FIELDS = ["id", "name", "company", "url", "official_urls", "datacenter_locations", "support_language"]
REQUIRED_PROVIDER_OFFICIAL_URL_FIELDS = ["top", "pricing", "specs", "support", "terms"]
REQUIRED_OFFICIAL_URL_ENTRY_FIELDS = ["url", "verified_at"]
REQUIRED_FEATURE_FIELDS = ["id", "category", "label", "description", "type"]
REQUIRED_EVIDENCE_FIELDS = [
    "provider_id", "feature_id", "value",
    "source_type", "source_url", "verified_at", "verification_status",
]
REQUIRED_BENCHMARK_FIELDS = ["provider_id", "plan", "tests"]
REQUIRED_BENCHMARK_TEST_FIELDS = ["metric", "value", "tool", "measured_at", "measured_by"]

VALID_FEATURE_TYPES = {"number", "boolean", "string"}
VALID_CATEGORIES = {"BASIC", "PRICE", "SPEC", "STORAGE", "NETWORK", "SECURITY", "BACKUP", "OPS", "SUPPORT", "BENCH"}
VALID_SOURCE_TYPES = {"official", "benchmark", "manual", "community", "unknown"}
VALID_VERIFICATION_STATUSES = {"verified", "unverified", "unknown"}

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_ID_RE = re.compile(r"^[a-z0-9-]+$")

errors: list[str] = []


def _is_valid_https_url(url: str) -> bool:
    """https:// で始まる有効な URL かどうかを検証する。"""
    if not url.startswith("https://"):
        return False
    parsed = urlparse(url)
    return bool(parsed.scheme == "https" and parsed.netloc)


def load_yaml(path: Path) -> dict | list:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_required_fields(item: dict, required: list[str], context: str) -> None:
    for field in required:
        if field not in item:
            errors.append(f"{context}: 必須フィールド '{field}' が存在しません。")


def validate_providers(data: dict) -> set[str]:
    provider_ids: set[str] = set()
    providers = data.get("providers", [])
    if not isinstance(providers, list):
        errors.append("providers.yml: 'providers' キーがリストではありません。")
        return provider_ids
    for i, provider in enumerate(providers):
        ctx = f"providers.yml[{i}] (id={provider.get('id', '?')})"
        check_required_fields(provider, REQUIRED_PROVIDER_FIELDS, ctx)

        # id のフォーマット・重複検証
        pid = provider.get("id")
        if pid is not None:
            if not str(pid).strip():
                errors.append(f"{ctx}: id が空文字です。")
            elif not _ID_RE.match(str(pid)):
                errors.append(
                    f"{ctx}: id '{pid}' は英小文字・数字・ハイフンのみ使用できます（例: my-provider）。"
                )
        if pid:
            if pid in provider_ids:
                errors.append(f"{ctx}: id '{pid}' が重複しています。")
            provider_ids.add(pid)

        # name の空文字検証
        pname = provider.get("name")
        if pname is not None and not str(pname).strip():
            errors.append(f"{ctx}: name が空文字です。")

        # url (website) の https:// 検証
        purl = provider.get("url")
        if purl is not None:
            if not _is_valid_https_url(str(purl)):
                errors.append(
                    f"{ctx}: url '{purl}' は https:// で始まる有効なURLである必要があります。"
                )

        official_urls = provider.get("official_urls")
        if official_urls is not None:
            if not isinstance(official_urls, dict):
                errors.append(f"{ctx}: 'official_urls' フィールドは辞書である必要があります。")
            else:
                check_required_fields(official_urls, REQUIRED_PROVIDER_OFFICIAL_URL_FIELDS, f"{ctx}.official_urls")
                for key, value in official_urls.items():
                    entry_ctx = f"{ctx}.official_urls.{key}"
                    if not isinstance(value, dict):
                        errors.append(
                            f"{entry_ctx}: 値は辞書（url / verified_at）である必要があります。"
                        )
                    else:
                        check_required_fields(value, REQUIRED_OFFICIAL_URL_ENTRY_FIELDS, entry_ctx)
                        url = value.get("url")
                        if url is not None and str(url) != "unknown":
                            if not _is_valid_https_url(str(url)):
                                errors.append(
                                    f"{entry_ctx}: url '{url}' は https:// で始まる有効なURLまたは 'unknown' である必要があります。"
                                )
                        vat = value.get("verified_at")
                        if vat is not None and str(vat) != "unknown":
                            if not _DATE_RE.match(str(vat)):
                                errors.append(
                                    f"{entry_ctx}: verified_at '{vat}' は YYYY-MM-DD 形式または 'unknown' である必要があります。"
                                )
    return provider_ids


def validate_features(data: dict) -> set[str]:
    feature_ids: set[str] = set()
    features = data.get("features", [])
    if not isinstance(features, list):
        errors.append("features.yml: 'features' キーがリストではありません。")
        return feature_ids
    for i, feature in enumerate(features):
        ctx = f"features.yml[{i}] (id={feature.get('id', '?')})"
        check_required_fields(feature, REQUIRED_FEATURE_FIELDS, ctx)
        fid = feature.get("id")
        if fid:
            if fid in feature_ids:
                errors.append(f"{ctx}: id '{fid}' が重複しています。")
            feature_ids.add(fid)
        fcat = feature.get("category")
        if fcat and fcat not in VALID_CATEGORIES:
            errors.append(f"{ctx}: category '{fcat}' は有効なカテゴリではありません（{sorted(VALID_CATEGORIES)}）。")
        ftype = feature.get("type")
        if ftype and ftype not in VALID_FEATURE_TYPES:
            errors.append(f"{ctx}: type '{ftype}' は有効な型ではありません（{VALID_FEATURE_TYPES}）。")
    return feature_ids


def validate_evidence(data: list, provider_ids: set[str], feature_ids: set[str]) -> None:
    evidence = data.get("evidence", [])
    if not isinstance(evidence, list):
        errors.append("evidence.yml: 'evidence' キーがリストではありません。")
        return
    seen: set[tuple[str, str]] = set()
    for i, entry in enumerate(evidence):
        pid = entry.get("provider_id", "?")
        fid = entry.get("feature_id", "?")
        ctx = f"evidence.yml[{i}] (provider_id={pid}, feature_id={fid})"
        check_required_fields(entry, REQUIRED_EVIDENCE_FIELDS, ctx)
        if pid != "?" and pid not in provider_ids:
            errors.append(f"{ctx}: provider_id '{pid}' は providers.yml に存在しません。")
        if fid != "?" and fid not in feature_ids:
            errors.append(f"{ctx}: feature_id '{fid}' は features.yml に存在しません。")
        key = (pid, fid)
        if key in seen:
            errors.append(f"{ctx}: (provider_id, feature_id) の組み合わせが重複しています。")
        seen.add(key)

        # source_type の検証
        stype = entry.get("source_type")
        if stype is not None and str(stype) not in VALID_SOURCE_TYPES:
            errors.append(
                f"{ctx}: source_type '{stype}' は有効な値ではありません"
                f"（{sorted(VALID_SOURCE_TYPES)}）。"
            )

        # source_url の検証（unknown または http/https URL）
        surl = entry.get("source_url")
        if surl is not None and str(surl) != "unknown":
            if not (str(surl).startswith("http://") or str(surl).startswith("https://")):
                errors.append(
                    f"{ctx}: source_url '{surl}' は有効なURLまたは 'unknown' である必要があります。"
                )

        # verified_at の検証（unknown または YYYY-MM-DD）
        vat = entry.get("verified_at")
        if vat is not None and str(vat) != "unknown":
            if not _DATE_RE.match(str(vat)):
                errors.append(
                    f"{ctx}: verified_at '{vat}' は YYYY-MM-DD 形式または 'unknown' である必要があります。"
                )

        # verification_status の検証
        vstatus = entry.get("verification_status")
        if vstatus is not None and str(vstatus) not in VALID_VERIFICATION_STATUSES:
            errors.append(
                f"{ctx}: verification_status '{vstatus}' は有効な値ではありません"
                f"（{sorted(VALID_VERIFICATION_STATUSES)}）。"
            )


def validate_benchmarks(data: dict, provider_ids: set[str]) -> None:
    benchmarks = data.get("benchmarks", [])
    if not isinstance(benchmarks, list):
        errors.append("benchmarks.yml: 'benchmarks' キーがリストではありません。")
        return
    for i, entry in enumerate(benchmarks):
        pid = entry.get("provider_id", "?")
        ctx = f"benchmarks.yml[{i}] (provider_id={pid})"
        check_required_fields(entry, REQUIRED_BENCHMARK_FIELDS, ctx)
        if pid != "?" and pid not in provider_ids:
            errors.append(f"{ctx}: provider_id '{pid}' は providers.yml に存在しません。")
        tests = entry.get("tests", [])
        if not isinstance(tests, list):
            errors.append(f"{ctx}: 'tests' フィールドがリストではありません。")
            continue
        for j, test in enumerate(tests):
            tctx = f"{ctx}.tests[{j}] (metric={test.get('metric', '?')})"
            check_required_fields(test, REQUIRED_BENCHMARK_TEST_FIELDS, tctx)


def main() -> int:
    files = {
        "providers": ROOT / "providers.yml",
        "features": ROOT / "features.yml",
        "evidence": ROOT / "evidence.yml",
        "benchmarks": ROOT / "benchmarks.yml",
    }

    missing = [str(p) for p in files.values() if not p.exists()]
    if missing:
        for m in missing:
            print(f"[ERROR] ファイルが見つかりません: {m}", file=sys.stderr)
        return 1

    providers_data = load_yaml(files["providers"])
    features_data = load_yaml(files["features"])
    evidence_data = load_yaml(files["evidence"])
    benchmarks_data = load_yaml(files["benchmarks"])

    provider_ids = validate_providers(providers_data)
    feature_ids = validate_features(features_data)
    validate_evidence(evidence_data, provider_ids, feature_ids)
    validate_benchmarks(benchmarks_data, provider_ids)

    if errors:
        for e in errors:
            print(f"[ERROR] {e}", file=sys.stderr)
        print(f"\n検証失敗: {len(errors)} 件のエラーが見つかりました。", file=sys.stderr)
        return 1

    print(f"検証成功: エラーなし（providers={len(provider_ids)}, features={len(feature_ids)}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
