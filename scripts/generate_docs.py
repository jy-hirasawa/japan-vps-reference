#!/usr/bin/env python3
"""
generate_docs.py — YAML ファイルから Markdown 比較テーブルを生成するスクリプト

使い方:
    python scripts/generate_docs.py

出力:
    docs/comparison.md  — プロバイダー比較テーブル
    docs/providers.md   — プロバイダー詳細一覧
    docs/update_candidates.md — 未確認項目更新候補一覧
    docs/use-cases.md   — 用途別比較ページ
"""

import sys
import yaml
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"

UNKNOWN_LABEL = "不明"


def load_yaml(path: Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _build_category_order_and_labels(categories: list) -> tuple[list[str], dict[str, str]]:
    """features.yml の categories セクションからカテゴリ順とラベルを構築する。"""
    order = [c["id"] for c in categories if "id" in c]
    labels = {c["id"]: c.get("label", c["id"]) for c in categories if "id" in c}
    return order, labels


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
    first_line_parts = [value]

    source_url = entry.get("source_url")
    if is_known_metadata(source_url):
        first_line_parts.append(f"[🔗]({source_url})")

    first_line = " ".join(first_line_parts)

    verified_at = entry.get("verified_at")
    if is_known_metadata(verified_at):
        return f"{first_line}<br>({verified_at})"

    return first_line


def build_evidence_map(evidence_list: list) -> dict[tuple[str, str], dict]:
    """(provider_id, feature_id) -> evidence エントリのマップを構築する。"""
    mapping: dict[tuple[str, str], dict] = {}
    for entry in evidence_list:
        key = (entry["provider_id"], entry["feature_id"])
        mapping[key] = entry
    return mapping


def collect_provider_latest_verified_at(providers: list, evidence_list: list) -> dict[str, str]:
    """各プロバイダーの evidence.yml における最新の verified_at を収集する。

    verified_at が unknown または未設定のエントリは無視する。
    有効な日付がないプロバイダーは「未確認」を返す。
    """
    latest: dict[str, str] = {}
    for entry in evidence_list:
        pid = entry.get("provider_id")
        verified_at = entry.get("verified_at")
        if pid is None or not is_known_metadata(verified_at):
            continue
        current = latest.get(pid)
        if current is None or str(verified_at) > current:
            latest[pid] = str(verified_at)

    result: dict[str, str] = {}
    for provider in providers:
        pid = provider["id"]
        result[pid] = latest.get(pid, "未確認")
    return result


def generate_evidence_verified_at_section(providers: list, evidence_list: list) -> list[str]:
    """Providerごとの最終確認日テーブルを生成する。"""
    latest = collect_provider_latest_verified_at(providers, evidence_list)
    lines: list[str] = []
    lines.append("## 最終確認日")
    lines.append("")
    lines.append("| Provider | 最終確認日 |")
    lines.append("| --- | --- |")
    for provider in providers:
        pid = provider["id"]
        lines.append(f"| {provider['name']} | {latest[pid]} |")
    lines.append("")
    return lines


OFFICIAL_URL_LABELS: dict[str, str] = {
    "top": "公式サイト",
    "pricing": "料金ページ",
    "specs": "仕様ページ",
    "support": "サポートページ",
    "terms": "利用規約",
}

OFFICIAL_URL_ORDER = ["top", "pricing", "specs", "support", "terms"]
STALE_DAYS = 180
PRIORITY_HIGH_CATEGORIES = {
    "BASIC",
    "PRICE",
    "SPEC",
    "STORAGE",
    "NETWORK",
    "BACKUP",
    "OS_TEMPLATE",
    "SUPPORT",
}
PRIORITY_MEDIUM_CATEGORIES = {"OPS", "SECURITY", "automation", "datacenter"}
PRIORITY_LABELS = ("高", "中", "低")
PRIORITY_SORT_ORDER = {"高": 0, "中": 1, "低": 2}


def _latest_verified_at(official_urls: dict) -> str:
    """official_urls の中から最新の verified_at を返す。すべて unknown なら「未確認」を返す。"""
    known_dates = [
        entry["verified_at"]
        for entry in official_urls.values()
        if isinstance(entry, dict) and is_known_metadata(entry.get("verified_at"))
    ]
    if not known_dates:
        return "未確認"
    return sorted(known_dates)[-1]


def generate_official_urls_section(providers: list) -> list[str]:
    """各プロバイダーの公式URLテーブルを生成する。"""
    lines: list[str] = []
    lines.append("## 公式URL")
    lines.append("")

    for provider in providers:
        lines.append(f"### {provider['name']}")
        lines.append("")
        lines.append("| 項目 | URL |")
        lines.append("| --- | --- |")

        official_urls: dict = provider.get("official_urls") or {}

        for key in OFFICIAL_URL_ORDER:
            entry = official_urls.get(key)
            label = OFFICIAL_URL_LABELS.get(key, key)
            if entry is None:
                continue
            url = entry.get("url") if isinstance(entry, dict) else str(entry)
            if is_known_metadata(url):
                lines.append(f"| {label} | [{url}]({url}) |")
            # unknown URLs are omitted per issue policy

        verified = _latest_verified_at(official_urls)
        lines.append(f"| 最終確認日 | {verified} |")
        lines.append("")

    return lines


def classify_update_status(url: str, verified_at: str, today: date) -> str:
    """URL/verified_at から更新ステータスを判定する。"""
    if not is_known_metadata(url) or not is_known_metadata(verified_at):
        return "UNKNOWN"

    try:
        verified_date = date.fromisoformat(str(verified_at))
    except ValueError:
        return "UNKNOWN"

    if verified_date <= today - timedelta(days=STALE_DAYS):
        return "STALE"
    return "VERIFIED"


def classify_priority_by_category(category_id: str) -> str:
    if category_id in PRIORITY_HIGH_CATEGORIES:
        return "高"
    if category_id in PRIORITY_MEDIUM_CATEGORIES:
        return "中"
    return "低"


def generate_update_candidates_page(
    providers: list,
    features: list,
    evidence_list: list,
    category_labels: dict[str, str] | None = None,
    today: date | None = None,
) -> str:
    if category_labels is None:
        category_labels = {}
    if today is None:
        today = date.today()

    evidence_map = build_evidence_map(evidence_list)
    provider_count = len(providers)
    provider_unknown_counts: dict[str, dict[str, int | str]] = {}
    for provider in providers:
        provider_unknown_counts[provider["id"]] = {
            "name": provider.get("name", UNKNOWN_LABEL),
            "高": 0,
            "中": 0,
            "低": 0,
            "total": 0,
        }

    category_unknown_counts: dict[str, dict[str, int | str]] = {}
    feature_unknown_rows: list[dict[str, int | str]] = []

    for feature in features:
        feature_id = str(feature.get("id", "unknown"))
        feature_label = str(feature.get("label", feature_id))
        category_id = str(feature.get("category", "OTHER"))
        category_label = str(category_labels.get(category_id, category_id))
        priority = classify_priority_by_category(category_id)
        unknown_count = 0
        official_source_count = 0

        for provider in providers:
            provider_id = provider["id"]
            entry = evidence_map.get((provider_id, feature_id))
            value = entry.get("value") if isinstance(entry, dict) else "unknown"
            source_type = entry.get("source_type") if isinstance(entry, dict) else "unknown"
            source_url = entry.get("source_url") if isinstance(entry, dict) else "unknown"

            if source_type == "official" and is_known_metadata(source_url):
                official_source_count += 1

            if str(value).strip().lower() == "unknown":
                unknown_count += 1
                provider_unknown_counts[provider_id][priority] = int(provider_unknown_counts[provider_id][priority]) + 1
                provider_unknown_counts[provider_id]["total"] = int(provider_unknown_counts[provider_id]["total"]) + 1

        if category_id not in category_unknown_counts:
            category_unknown_counts[category_id] = {
                "category_label": category_label,
                "priority": priority,
                "unknown": 0,
                "total": 0,
            }
        category_unknown_counts[category_id]["unknown"] = int(category_unknown_counts[category_id]["unknown"]) + unknown_count
        category_unknown_counts[category_id]["total"] = int(category_unknown_counts[category_id]["total"]) + provider_count

        feature_unknown_rows.append(
            {
                "feature_label": feature_label,
                "category_label": category_label,
                "priority": priority,
                "unknown_count": unknown_count,
                "official_source_count": official_source_count,
            }
        )

    category_rows = sorted(
        category_unknown_counts.values(),
        key=lambda row: (
            PRIORITY_SORT_ORDER[str(row["priority"])],
            -int(row["unknown"]),
            str(row["category_label"]),
        ),
    )
    provider_rows = sorted(
        provider_unknown_counts.values(),
        key=lambda row: (
            -int(row["高"]),
            -int(row["total"]),
            str(row["name"]),
        ),
    )
    next_research_rows = sorted(
        [
            row
            for row in feature_unknown_rows
            if str(row["priority"]) == "高"
            and int(row["unknown_count"]) > 0
            and int(row["official_source_count"]) > 0
        ],
        key=lambda row: (-int(row["unknown_count"]), str(row["category_label"]), str(row["feature_label"])),
    )
    hard_to_verify_rows = sorted(
        [
            row
            for row in feature_unknown_rows
            if int(row["unknown_count"]) == provider_count and int(row["official_source_count"]) == 0
        ],
        key=lambda row: (
            PRIORITY_SORT_ORDER[str(row["priority"])],
            str(row["category_label"]),
            str(row["feature_label"]),
        ),
    )

    lines: list[str] = []
    lines.append("# 未確認項目の更新候補一覧")
    lines.append("")
    lines.append("> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。")
    lines.append("> `unknown` のまま残っている項目を優先度付きで整理し、次に調査すべき項目を示します。")
    lines.append(f"> `verified_at` が `{STALE_DAYS}` 日以上前の項目は `STALE` と表示します。")
    lines.append("")
    lines.append("## 優先度定義")
    lines.append("")
    lines.append(f"- 高: {', '.join(sorted(PRIORITY_HIGH_CATEGORIES))}")
    lines.append(f"- 中: {', '.join(sorted(PRIORITY_MEDIUM_CATEGORIES))}")
    lines.append("- 低: 上記以外のカテゴリ")
    lines.append("")
    lines.append("## カテゴリ別 unknown 集計")
    lines.append("")
    lines.append("| 優先度 | カテゴリ | unknown / 総項目数 | unknown率 |")
    lines.append("| --- | --- | --- | --- |")
    for row in category_rows:
        unknown_count = int(row["unknown"])
        total_count = int(row["total"])
        ratio = 0 if total_count == 0 else int((unknown_count / total_count) * 100)
        lines.append(
            f"| {row['priority']} | {row['category_label']} | {unknown_count} / {total_count} | {ratio}% |"
        )
    lines.append("")
    lines.append("## プロバイダー別 unknown 集計")
    lines.append("")
    lines.append("| Provider | 高 | 中 | 低 | 合計 |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in provider_rows:
        lines.append(f"| {row['name']} | {row['高']} | {row['中']} | {row['低']} | {row['total']} |")
    lines.append("")
    lines.append("## 次に調査すべき項目（優先度: 高）")
    lines.append("")
    if next_research_rows:
        lines.append("| カテゴリ | 項目 | unknown の Provider 数 | 公式URL付き根拠あり Provider 数 |")
        lines.append("| --- | --- | --- | --- |")
        for row in next_research_rows:
            lines.append(
                f"| {row['category_label']} | {row['feature_label']} | {row['unknown_count']} / {provider_count} | {row['official_source_count']} / {provider_count} |"
            )
    else:
        lines.append("（該当なし）")
    lines.append("")
    lines.append("## 公式情報で確認しづらい項目")
    lines.append("")
    lines.append("> 全プロバイダーで `unknown` かつ、`source_type: official` + `source_url` 付き根拠が未登録の項目です。")
    lines.append("")
    if hard_to_verify_rows:
        lines.append("| 優先度 | カテゴリ | 項目 |")
        lines.append("| --- | --- | --- |")
        for row in hard_to_verify_rows:
            lines.append(f"| {row['priority']} | {row['category_label']} | {row['feature_label']} |")
    else:
        lines.append("（該当なし）")
    lines.append("")
    lines.append("## 公式URL更新候補")
    lines.append("")
    lines.append("| Provider | Item | URL | verified_at | Status |")
    lines.append("| --- | --- | --- | --- | --- |")

    for provider in providers:
        official_urls: dict = provider.get("official_urls") or {}
        provider_name = provider.get("name", UNKNOWN_LABEL)

        for item in OFFICIAL_URL_ORDER:
            entry = official_urls.get(item)
            if isinstance(entry, dict):
                url = str(entry.get("url", "unknown"))
                verified_at = str(entry.get("verified_at", "unknown"))
            else:
                url = "unknown"
                verified_at = "unknown"

            status = classify_update_status(url, verified_at, today)
            lines.append(f"| {provider_name} | {item} | {url} | {verified_at} | {status} |")

    lines.append("")
    return "\n".join(lines)


def generate_comparison_table(
    providers: list,
    features: list,
    evidence_map: dict[tuple[str, str], dict],
    category_order: list[str] | None = None,
    category_labels: dict[str, str] | None = None,
    evidence_list: list | None = None,
) -> str:
    if category_order is None:
        category_order = []
    if category_labels is None:
        category_labels = {}
    if evidence_list is None:
        evidence_list = []

    lines: list[str] = []
    lines.append("# VPS 比較テーブル")
    lines.append("")
    lines.append("> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。")
    lines.append("> 「不明」は公式情報が確認できないことを示します。")
    lines.append("> 値の横の `🔗` は情報源リンク、`(YYYY-MM-DD)` は確認日です。")
    lines.append("")
    lines.extend(generate_evidence_verified_at_section(providers, evidence_list))
    lines.extend(generate_official_urls_section(providers))
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

    # features.yml の categories 定義順に出力
    ordered_categories = [c for c in category_order if c in features_by_category]
    # categories に含まれないカテゴリがあれば末尾に追加
    for cat in sorted(features_by_category):
        if cat not in ordered_categories:
            ordered_categories.append(cat)

    header_cells = ["#", "項目"] + [p["name"] for p in providers]
    header_row = "| " + " | ".join(header_cells) + " |"
    separator_row = "| " + " | ".join(["---"] * len(header_cells)) + " |"

    for cat in ordered_categories:
        cat_label = category_labels.get(cat, cat)
        lines.append(f"## {cat_label}")
        lines.append("")
        lines.append(header_row)
        lines.append(separator_row)
        for row_num, feature in enumerate(features_by_category[cat], start=1):
            fid = feature["id"]
            ftype = feature.get("type", "string")
            row_cells = [str(row_num), feature["label"]]
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
        for row_num, feature in enumerate(uncategorized, start=1):
            fid = feature["id"]
            ftype = feature.get("type", "string")
            row_cells = [str(row_num), feature["label"]]
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
    lines.append("| ✅ | 対応あり（確認済み） |")
    lines.append("| ❌ | 非対応（確認済み） |")
    lines.append("| `-` | プランなし・該当なし（確認済み） |")
    lines.append("| 不明 | 公式情報が確認できていない |")
    lines.append("")
    lines.append("> 値の表現ルールの詳細は [docs/data-policy.md](data-policy.md) を参照してください。")
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


USE_CASES: list[dict] = [
    {
        "id": "low-cost",
        "label": "低価格重視",
        "description": "初期費用・月額料金を抑えたい場合の比較項目です。",
        "feature_ids": [
            "min_price_jpy",
            "price_2gb_monthly",
            "price_2gb_hourly",
            "price_4gb_monthly",
            "price_4gb_hourly",
            "monthly_cap",
            "initial_cost",
            "min_contract_period",
        ],
    },
    {
        "id": "dev-staging",
        "label": "開発・検証環境",
        "description": "開発・検証用途で重要な自動化・スクリプト・スナップショット等の比較項目です。",
        "feature_ids": [
            "startup_script",
            "cloud_init",
            "docker_template",
            "custom_iso",
            "api_available",
            "cli_available",
            "terraform_provider",
            "ssh_key",
            "full_disk_snapshot",
            "auto_snapshot",
        ],
    },
    {
        "id": "wordpress",
        "label": "WordPress / Webサイト運用",
        "description": "WordPressやWebサイト運用に関連する比較項目です。",
        "feature_ids": [
            "app_template",
            "kusanagi_template",
            "min_price_jpy",
            "price_2gb_monthly",
            "backup_feature",
            "auto_backup",
            "full_disk_snapshot",
            "firewall_feature",
            "ddos_protection",
            "load_balancer",
            "sla_uptime_percent",
        ],
    },
    {
        "id": "production",
        "label": "本番サービス運用",
        "description": "本番環境での安定稼働・冗長性・セキュリティに関する比較項目です。",
        "feature_ids": [
            "sla_uptime_percent",
            "sla_document_url",
            "load_balancer",
            "private_network",
            "auto_backup",
            "backup_retention_period",
            "firewall_feature",
            "ddos_protection",
            "status_page",
            "incident_page",
            "domestic_region_count",
            "multi_region_deployment",
            "iso27001",
            "isms",
        ],
    },
    {
        "id": "backup-dr",
        "label": "バックアップ・DR重視",
        "description": "バックアップ・障害復旧（DR）対応に関する比較項目です。",
        "feature_ids": [
            "manual_backup",
            "auto_backup",
            "backup_schedule",
            "backup_retention_period",
            "backup_generations",
            "restore_from_backup",
            "backup_encryption",
            "backup_to_object_storage",
            "cross_region_backup",
            "dr_support",
            "full_disk_snapshot",
            "auto_snapshot",
            "backup_billing",
        ],
    },
    {
        "id": "automation",
        "label": "API / IaC による自動化重視",
        "description": "REST API・CLI・Terraform等の自動化ツール対応に関する比較項目です。",
        "feature_ids": [
            "api_available",
            "openapi_published",
            "cli_available",
            "terraform_provider",
            "pulumi_support",
            "ansible_support",
            "metadata_service",
            "api_rate_limit_published",
            "webhook",
            "sdk_go",
            "sdk_python",
            "sdk_nodejs",
            "startup_script",
            "cloud_init",
        ],
    },
]


def generate_use_cases_page(
    providers: list,
    features: list,
    evidence_map: dict[tuple[str, str], dict],
) -> str:
    """用途別比較ページを生成する。"""
    feature_index: dict[str, dict] = {f["id"]: f for f in features}

    lines: list[str] = []
    lines.append("# 用途別 VPS 比較")
    lines.append("")
    lines.append("> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。")
    lines.append("> 「不明」は公式情報が確認できないことを示します。推測によるおすすめ順位付けは行っていません。")
    lines.append("")

    for use_case in USE_CASES:
        lines.append(f"## {use_case['label']}")
        lines.append("")
        lines.append(f"> {use_case['description']}")
        lines.append("")

        # 存在する feature_id のみに絞り込む
        uc_features = [
            feature_index[fid]
            for fid in use_case["feature_ids"]
            if fid in feature_index
        ]

        if not uc_features:
            lines.append("（対応する比較項目がありません）")
            lines.append("")
            continue

        header_cells = ["項目"] + [p["name"] for p in providers]
        lines.append("| " + " | ".join(header_cells) + " |")
        lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")

        for feature in uc_features:
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
    lines.append("| ✅ | 対応あり（確認済み） |")
    lines.append("| ❌ | 非対応（確認済み） |")
    lines.append("| `-` | プランなし・該当なし（確認済み） |")
    lines.append("| 不明 | 公式情報が確認できていない |")
    lines.append("")
    lines.append("> 値の表現ルールの詳細は [docs/data-policy.md](data-policy.md) を参照してください。")
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
    categories = features_data.get("categories", [])
    evidence_list = evidence_data.get("evidence", [])

    evidence_map = build_evidence_map(evidence_list)
    category_order, category_labels = _build_category_order_and_labels(categories)

    DOCS_DIR.mkdir(exist_ok=True)

    comparison_md = generate_comparison_table(providers, features, evidence_map, category_order, category_labels, evidence_list)
    comparison_path = DOCS_DIR / "comparison.md"
    comparison_path.write_text(comparison_md, encoding="utf-8")
    print(f"生成しました: {comparison_path.relative_to(ROOT)}")

    providers_md = generate_providers_page(providers)
    providers_path = DOCS_DIR / "providers.md"
    providers_path.write_text(providers_md, encoding="utf-8")
    print(f"生成しました: {providers_path.relative_to(ROOT)}")

    update_candidates_md = generate_update_candidates_page(providers, features, evidence_list, category_labels)
    update_candidates_path = DOCS_DIR / "update_candidates.md"
    update_candidates_path.write_text(update_candidates_md, encoding="utf-8")
    print(f"生成しました: {update_candidates_path.relative_to(ROOT)}")

    use_cases_md = generate_use_cases_page(providers, features, evidence_map)
    use_cases_path = DOCS_DIR / "use-cases.md"
    use_cases_path.write_text(use_cases_md, encoding="utf-8")
    print(f"生成しました: {use_cases_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
