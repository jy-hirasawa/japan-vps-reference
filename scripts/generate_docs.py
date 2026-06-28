#!/usr/bin/env python3
"""
generate_docs.py — YAML ファイルから Markdown 比較テーブルを生成するスクリプト

使い方:
    python scripts/generate_docs.py

出力:
    docs/comparison.md  — プロバイダー比較テーブル
    docs/providers.md   — プロバイダー詳細一覧
"""

import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"

UNKNOWN_LABEL = "不明"

CATEGORY_ORDER = ["BASIC", "PRICE", "SPEC", "STORAGE", "NETWORK", "SECURITY", "BACKUP", "OPS", "SUPPORT", "BENCH"]
CATEGORY_LABELS = {
    "BASIC": "基本情報",
    "PRICE": "料金",
    "SPEC": "CPU / メモリ / ストレージ",
    "STORAGE": "ディスク / NVMe / スナップショット",
    "NETWORK": "IPv4 / IPv6 / 転送量 / ローカルネットワーク",
    "SECURITY": "Firewall / WAF / DDoS",
    "BACKUP": "バックアップ / イメージ保存",
    "OPS": "API / CLI / Terraform",
    "SUPPORT": "サポート / SLA",
    "BENCH": "ベンチマーク",
}


def load_yaml(path: Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_value(raw, feature_type: str) -> str:
    """値を表示用にフォーマットする。unknown は「不明」に変換する。"""
    if raw is None or str(raw).strip().lower() == "unknown":
        return UNKNOWN_LABEL
    if feature_type == "boolean":
        return "✅" if raw is True else "❌"
    return str(raw)


def is_known_metadata(raw) -> bool:
    return raw is not None and str(raw).strip() != "" and str(raw).strip().lower() != "unknown"


def format_comparison_cell(entry: dict, feature_type: str) -> str:
    value = format_value(entry.get("value"), feature_type)
    parts = [value]

    source_url = entry.get("source_url")
    if is_known_metadata(source_url):
        parts.append(f"[🔗]({source_url})")

    verified_at = entry.get("verified_at")
    if is_known_metadata(verified_at):
        parts.append(f"({verified_at})")

    return " ".join(parts)


def build_evidence_map(evidence_list: list) -> dict[tuple[str, str], dict]:
    """(provider_id, feature_id) -> evidence エントリのマップを構築する。"""
    mapping: dict[tuple[str, str], dict] = {}
    for entry in evidence_list:
        key = (entry["provider_id"], entry["feature_id"])
        mapping[key] = entry
    return mapping


def generate_comparison_table(
    providers: list,
    features: list,
    evidence_map: dict[tuple[str, str], dict],
) -> str:
    lines: list[str] = []
    lines.append("# VPS 比較テーブル")
    lines.append("")
    lines.append("> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。")
    lines.append("> 「不明」は公式情報が確認できないことを示します。")
    lines.append("> 値の横の `🔗` は情報源リンク、`(YYYY-MM-DD)` は確認日です。")
    lines.append("")

    # カテゴリ別にfeaturesを分類
    features_by_category: dict[str, list] = {}
    uncategorized: list = []
    for feature in features:
        cat = feature.get("category")
        if cat:
            features_by_category.setdefault(cat, []).append(feature)
        else:
            uncategorized.append(feature)

    # カテゴリ順に出力
    ordered_categories = [c for c in CATEGORY_ORDER if c in features_by_category]
    # CATEGORY_ORDERにないカテゴリがあれば末尾に追加
    for cat in sorted(features_by_category):
        if cat not in ordered_categories:
            ordered_categories.append(cat)

    header_cells = ["機能 / プロバイダー"] + [p["name"] for p in providers]
    header_row = "| " + " | ".join(header_cells) + " |"
    separator_row = "| " + " | ".join(["---"] * len(header_cells)) + " |"

    for cat in ordered_categories:
        cat_label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f"## {cat}: {cat_label}")
        lines.append("")
        lines.append(header_row)
        lines.append(separator_row)
        for feature in features_by_category[cat]:
            fid = feature["id"]
            ftype = feature.get("type", "string")
            row_cells = [feature["label"]]
            for provider in providers:
                pid = provider["id"]
                entry = evidence_map.get((pid, fid))
                if entry is None:
                    row_cells.append(UNKNOWN_LABEL)
                else:
                    row_cells.append(format_comparison_cell(entry, ftype))
            lines.append("| " + " | ".join(row_cells) + " |")
        lines.append("")

    # カテゴリなし項目（後方互換）
    if uncategorized:
        lines.append("## その他")
        lines.append("")
        lines.append(header_row)
        lines.append(separator_row)
        for feature in uncategorized:
            fid = feature["id"]
            ftype = feature.get("type", "string")
            row_cells = [feature["label"]]
            for provider in providers:
                pid = provider["id"]
                entry = evidence_map.get((pid, fid))
                if entry is None:
                    row_cells.append(UNKNOWN_LABEL)
                else:
                    row_cells.append(format_comparison_cell(entry, ftype))
            lines.append("| " + " | ".join(row_cells) + " |")
        lines.append("")

    lines.append("## 凡例")
    lines.append("")
    lines.append("| 表示 | 意味 |")
    lines.append("| --- | --- |")
    lines.append("| ✅ | 対応あり |")
    lines.append("| ❌ | 非対応 |")
    lines.append("| 不明 | 公式情報が確認できていない |")
    lines.append("")

    return "\n".join(lines)


def generate_providers_page(providers: list) -> str:
    lines: list[str] = []
    lines.append("# プロバイダー詳細一覧")
    lines.append("")
    lines.append("> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。")
    lines.append("")

    for provider in providers:
        lines.append(f"## {provider['name']}")
        lines.append("")
        lines.append(f"- **会社名**: {provider.get('company', UNKNOWN_LABEL)}")
        lines.append(f"- **公式サイト**: {provider.get('url', UNKNOWN_LABEL)}")
        dc = provider.get("datacenter_locations")
        if dc and isinstance(dc, list) and not all(str(x).strip().lower() == "unknown" for x in dc):
            lines.append(f"- **データセンター**: {', '.join(dc)}")
        else:
            lines.append(f"- **データセンター**: {UNKNOWN_LABEL}")
        langs = provider.get("support_language")
        if langs and isinstance(langs, list):
            lines.append(f"- **サポート言語**: {', '.join(langs)}")
        else:
            lines.append(f"- **サポート言語**: {UNKNOWN_LABEL}")
        notes = provider.get("notes")
        if notes:
            lines.append(f"- **備考**: {notes}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    files = {
        "providers": ROOT / "providers.yml",
        "features": ROOT / "features.yml",
        "evidence": ROOT / "evidence.yml",
    }

    missing = [str(p.relative_to(ROOT)) for p in files.values() if not p.exists()]
    if missing:
        for m in missing:
            print(f"[ERROR] ファイルが見つかりません: {m}", file=sys.stderr)
        return 1

    providers_data = load_yaml(files["providers"])
    features_data = load_yaml(files["features"])
    evidence_data = load_yaml(files["evidence"])

    providers = providers_data.get("providers", [])
    features = features_data.get("features", [])
    evidence_list = evidence_data.get("evidence", [])

    evidence_map = build_evidence_map(evidence_list)

    DOCS_DIR.mkdir(exist_ok=True)

    comparison_md = generate_comparison_table(providers, features, evidence_map)
    comparison_path = DOCS_DIR / "comparison.md"
    comparison_path.write_text(comparison_md, encoding="utf-8")
    print(f"生成しました: {comparison_path.relative_to(ROOT)}")

    providers_md = generate_providers_page(providers)
    providers_path = DOCS_DIR / "providers.md"
    providers_path.write_text(providers_md, encoding="utf-8")
    print(f"生成しました: {providers_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
