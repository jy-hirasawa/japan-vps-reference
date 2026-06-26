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
    lines.append("")

    # ヘッダー行
    header_cells = ["機能 / プロバイダー"] + [p["name"] for p in providers]
    lines.append("| " + " | ".join(header_cells) + " |")
    lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")

    for feature in features:
        fid = feature["id"]
        ftype = feature.get("type", "string")
        row_cells = [feature["label"]]
        for provider in providers:
            pid = provider["id"]
            entry = evidence_map.get((pid, fid))
            if entry is None:
                row_cells.append(UNKNOWN_LABEL)
            else:
                row_cells.append(format_value(entry.get("value"), ftype))
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
        if dc and isinstance(dc, list):
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

    missing = [str(p) for p in files.values() if not p.exists()]
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
    print(f"生成しました: {comparison_path}")

    providers_md = generate_providers_page(providers)
    providers_path = DOCS_DIR / "providers.md"
    providers_path.write_text(providers_md, encoding="utf-8")
    print(f"生成しました: {providers_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
