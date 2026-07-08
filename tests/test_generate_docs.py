"""
tests/test_generate_docs.py — scripts/generate_docs.py の単体テスト
"""

import sys
import unittest
from pathlib import Path
from datetime import date
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import generate_docs


def _make_provider(pid: str = "test-vps", name: str = "Test VPS") -> dict:
    return {
        "id": pid,
        "name": name,
        "official_urls": {},
    }


def _make_feature(fid: str, label: str, category: str = "BASIC", ftype: str = "string") -> dict:
    return {
        "id": fid,
        "label": label,
        "category": category,
        "type": ftype,
    }


def _make_evidence(pid: str, fid: str, value, source_url: str = "unknown", verified_at: str = "unknown") -> dict:
    return {
        "provider_id": pid,
        "feature_id": fid,
        "value": value,
        "source_url": source_url,
        "verified_at": verified_at,
    }


_DEFAULT_CATEGORY_ORDER = ["BASIC", "PRICE", "SPEC", "STORAGE", "NETWORK",
                           "SECURITY", "BACKUP", "OPS", "SUPPORT", "BENCH"]
_DEFAULT_CATEGORY_LABELS = {
    "BASIC": "基本情報", "PRICE": "料金", "SPEC": "CPU / メモリ / ストレージ",
    "STORAGE": "ディスク / NVMe / スナップショット",
    "NETWORK": "IPv4 / IPv6 / 転送量 / ローカルネットワーク",
    "SECURITY": "Firewall / WAF / DDoS", "BACKUP": "バックアップ / イメージ保存",
    "OPS": "API / CLI / Terraform", "SUPPORT": "サポート / SLA", "BENCH": "ベンチマーク",
}


class TestGenerateComparisonTable(unittest.TestCase):

    def _generate(self, providers, features, evidence_list=None,
                  category_order=None, category_labels=None):
        evidence_map = generate_docs.build_evidence_map(evidence_list or [])
        return generate_docs.generate_comparison_table(
            providers, features, evidence_map,
            category_order=category_order or _DEFAULT_CATEGORY_ORDER,
            category_labels=category_labels or _DEFAULT_CATEGORY_LABELS,
        )

    # ------------------------------------------------------------------
    # features.yml の定義順が反映される
    # ------------------------------------------------------------------

    def test_features_order_within_category(self):
        """同一カテゴリ内での features の順番が features.yml の記載順に従う。"""
        providers = [_make_provider()]
        features = [
            _make_feature("feat-z", "Z項目", category="BASIC"),
            _make_feature("feat-a", "A項目", category="BASIC"),
            _make_feature("feat-m", "M項目", category="BASIC"),
        ]
        md = self._generate(providers, features)
        pos_z = md.index("Z項目")
        pos_a = md.index("A項目")
        pos_m = md.index("M項目")
        self.assertLess(pos_z, pos_a, "Z項目 は A項目 より前に出力されるべき")
        self.assertLess(pos_a, pos_m, "A項目 は M項目 より前に出力されるべき")

    def test_category_order(self):
        """カテゴリは CATEGORY_ORDER に従って出力される。"""
        providers = [_make_provider()]
        features = [
            _make_feature("feat-ops", "OPS項目", category="OPS"),
            _make_feature("feat-basic", "BASIC項目", category="BASIC"),
            _make_feature("feat-price", "PRICE項目", category="PRICE"),
        ]
        md = self._generate(providers, features)
        pos_basic = md.index("BASIC")
        pos_price = md.index("PRICE")
        pos_ops = md.index("OPS")
        self.assertLess(pos_basic, pos_price, "BASIC は PRICE より前に出力されるべき")
        self.assertLess(pos_price, pos_ops, "PRICE は OPS より前に出力されるべき")

    def test_category_heading_uses_label_only(self):
        """カテゴリ見出しは label のみで出力され、カテゴリ ID は含まれない。"""
        providers = [_make_provider()]
        features = [_make_feature("feat-a", "A項目", category="BASIC")]
        md = self._generate(providers, features)
        self.assertIn("## 基本情報", md)
        self.assertNotIn("## BASIC:", md)

    # ------------------------------------------------------------------
    # 値のフォーマット
    # ------------------------------------------------------------------

    def test_boolean_true_displays_check(self):
        """boolean: true は ✅ として表示される。"""
        providers = [_make_provider("prov-a", "ProvA")]
        features = [_make_feature("feat-bool", "Bool項目", ftype="boolean")]
        evidence = [_make_evidence("prov-a", "feat-bool", True)]
        md = self._generate(providers, features, evidence)
        self.assertIn("✅", md)

    def test_boolean_false_displays_cross(self):
        """boolean: false は ❌ として表示される。"""
        providers = [_make_provider("prov-a", "ProvA")]
        features = [_make_feature("feat-bool", "Bool項目", ftype="boolean")]
        evidence = [_make_evidence("prov-a", "feat-bool", False)]
        md = self._generate(providers, features, evidence)
        self.assertIn("❌", md)

    def test_unknown_value_displays_unknown_label(self):
        """evidence が存在しない場合は「不明」と表示される。"""
        providers = [_make_provider("prov-a", "ProvA")]
        features = [_make_feature("feat-x", "X項目")]
        md = self._generate(providers, features, [])
        self.assertIn(generate_docs.UNKNOWN_LABEL, md)

    def test_number_value_displayed(self):
        """数値は文字列として表示される。"""
        providers = [_make_provider("prov-a", "ProvA")]
        features = [_make_feature("feat-num", "Num項目", ftype="number")]
        evidence = [_make_evidence("prov-a", "feat-num", 512)]
        md = self._generate(providers, features, evidence)
        self.assertIn("512", md)

    # ------------------------------------------------------------------
    # カテゴリなし項目（後方互換）
    # ------------------------------------------------------------------

    def test_uncategorized_feature_appears_in_other_section(self):
        """category なしの feature は「その他」セクションに出力される。"""
        providers = [_make_provider()]
        features = [{"id": "feat-nocat", "label": "カテゴリなし項目", "type": "string"}]
        md = self._generate(providers, features)
        self.assertIn("その他", md)
        self.assertIn("カテゴリなし項目", md)

    def test_repository_network_features_are_rendered(self):
        """実データの NETWORK 項目がネットワーク見出し配下に出力される。"""
        repo_root = Path(__file__).resolve().parent.parent
        features_data = yaml.safe_load((repo_root / "features.yml").read_text(encoding="utf-8"))
        network_features = [f for f in features_data["features"] if f["category"] == "NETWORK"]
        category_order, category_labels = generate_docs._build_category_order_and_labels(
            features_data["categories"]
        )

        md = self._generate(
            [_make_provider()],
            network_features,
            category_order=category_order,
            category_labels=category_labels,
        )

        self.assertIn("## ネットワーク", md)
        for label in [
            "IPv4",
            "IPv6",
            "追加IPv4",
            "逆引きDNS",
            "転送量制限",
            "帯域目安（Gbps）",
            "ローカルネットワーク",
            "プライベートネットワーク",
            "VLAN",
            "ロードバランサー",
            "Floating IP",
        ]:
            self.assertIn(label, md)

    def test_repository_security_features_are_rendered(self):
        """実データの SECURITY 項目がセキュリティ見出し配下に出力される。"""
        repo_root = Path(__file__).resolve().parent.parent
        features_data = yaml.safe_load((repo_root / "features.yml").read_text(encoding="utf-8"))
        security_features = [f for f in features_data["features"] if f["category"] == "SECURITY"]
        category_order, category_labels = generate_docs._build_category_order_and_labels(
            features_data["categories"]
        )

        md = self._generate(
            [_make_provider()],
            security_features,
            category_order=category_order,
            category_labels=category_labels,
        )

        self.assertIn("## セキュリティ", md)
        for label in [
            "SSH鍵ログイン",
            "ファイアウォール機能",
            "DDoS保護",
            "WAF",
            "セキュリティグループ",
            "二要素認証（管理画面）",
            "APIトークン",
            "IAM / 権限管理",
            "監査ログ",
            "ISO27001",
            "ISMS",
            "SOC 2",
            "PCI DSS",
            "データセンター認証",
        ]:
            self.assertIn(label, md)

    # ------------------------------------------------------------------
    # 凡例が含まれる
    # ------------------------------------------------------------------

    def test_legend_section_included(self):
        """生成された Markdown に凡例セクションが含まれる。"""
        providers = [_make_provider()]
        features = [_make_feature("feat-a", "A項目")]
        md = self._generate(providers, features)
        self.assertIn("凡例", md)
        self.assertIn("対応あり", md)
        self.assertIn("非対応", md)


class TestBuildEvidenceMap(unittest.TestCase):

    def test_build_evidence_map_basic(self):
        """(provider_id, feature_id) をキーとするマップが構築される。"""
        evidence_list = [
            {"provider_id": "p1", "feature_id": "f1", "value": "v1"},
            {"provider_id": "p1", "feature_id": "f2", "value": "v2"},
            {"provider_id": "p2", "feature_id": "f1", "value": "v3"},
        ]
        result = generate_docs.build_evidence_map(evidence_list)
        self.assertEqual(result[("p1", "f1")]["value"], "v1")
        self.assertEqual(result[("p1", "f2")]["value"], "v2")
        self.assertEqual(result[("p2", "f1")]["value"], "v3")

    def test_build_evidence_map_empty(self):
        """空リストを渡した場合は空のマップが返る。"""
        result = generate_docs.build_evidence_map([])
        self.assertEqual(result, {})


class TestBuildCategoryOrderAndLabels(unittest.TestCase):

    def test_basic(self):
        """categories リストから順序とラベルが正しく構築される。"""
        categories = [
            {"id": "BASIC", "label": "基本情報"},
            {"id": "PRICE", "label": "料金"},
            {"id": "OPS", "label": "API / CLI / Terraform"},
        ]
        order, labels = generate_docs._build_category_order_and_labels(categories)
        self.assertEqual(order, ["BASIC", "PRICE", "OPS"])
        self.assertEqual(labels["BASIC"], "基本情報")
        self.assertEqual(labels["PRICE"], "料金")
        self.assertEqual(labels["OPS"], "API / CLI / Terraform")

    def test_empty_categories(self):
        """空リストを渡した場合は空のリスト・辞書が返る。"""
        order, labels = generate_docs._build_category_order_and_labels([])
        self.assertEqual(order, [])
        self.assertEqual(labels, {})

    def test_category_order_preserved(self):
        """categories の記載順が category_order の並び順に反映される。"""
        categories = [
            {"id": "OPS", "label": "API"},
            {"id": "BASIC", "label": "基本"},
        ]
        order, _ = generate_docs._build_category_order_and_labels(categories)
        self.assertEqual(order, ["OPS", "BASIC"])


class TestCollectProviderLatestVerifiedAt(unittest.TestCase):

    def test_returns_latest_date_per_provider(self):
        """複数エントリがある場合は最新の verified_at を返す。"""
        providers = [_make_provider("p1", "P1")]
        evidence_list = [
            _make_evidence("p1", "f1", "v1", verified_at="2024-01-01"),
            _make_evidence("p1", "f2", "v2", verified_at="2024-06-15"),
            _make_evidence("p1", "f3", "v3", verified_at="2024-03-10"),
        ]
        result = generate_docs.collect_provider_latest_verified_at(providers, evidence_list)
        self.assertEqual(result["p1"], "2024-06-15")

    def test_ignores_unknown_verified_at(self):
        """verified_at が unknown のエントリは無視され、有効な日付のみ集計される。"""
        providers = [_make_provider("p1", "P1")]
        evidence_list = [
            _make_evidence("p1", "f1", "v1", verified_at="unknown"),
            _make_evidence("p1", "f2", "v2", verified_at="2024-05-01"),
        ]
        result = generate_docs.collect_provider_latest_verified_at(providers, evidence_list)
        self.assertEqual(result["p1"], "2024-05-01")

    def test_all_unknown_returns_unconfirmed(self):
        """有効な verified_at が存在しないプロバイダーは「未確認」を返す。"""
        providers = [_make_provider("p1", "P1")]
        evidence_list = [
            _make_evidence("p1", "f1", "v1", verified_at="unknown"),
        ]
        result = generate_docs.collect_provider_latest_verified_at(providers, evidence_list)
        self.assertEqual(result["p1"], "未確認")

    def test_no_evidence_returns_unconfirmed(self):
        """evidence が空の場合は全プロバイダーが「未確認」になる。"""
        providers = [_make_provider("p1", "P1"), _make_provider("p2", "P2")]
        result = generate_docs.collect_provider_latest_verified_at(providers, [])
        self.assertEqual(result["p1"], "未確認")
        self.assertEqual(result["p2"], "未確認")

    def test_multiple_providers_independent(self):
        """複数プロバイダーの最終確認日がそれぞれ独立して集計される。"""
        providers = [_make_provider("p1", "P1"), _make_provider("p2", "P2")]
        evidence_list = [
            _make_evidence("p1", "f1", "v1", verified_at="2024-01-01"),
            _make_evidence("p2", "f1", "v2", verified_at="2024-12-31"),
        ]
        result = generate_docs.collect_provider_latest_verified_at(providers, evidence_list)
        self.assertEqual(result["p1"], "2024-01-01")
        self.assertEqual(result["p2"], "2024-12-31")


class TestGenerateEvidenceVerifiedAtSection(unittest.TestCase):

    def test_section_contains_provider_name_and_date(self):
        """生成されたセクションにプロバイダー名と最終確認日が含まれる。"""
        providers = [_make_provider("p1", "テストVPS")]
        evidence_list = [_make_evidence("p1", "f1", "v1", verified_at="2024-06-20")]
        lines = generate_docs.generate_evidence_verified_at_section(providers, evidence_list)
        section = "\n".join(lines)
        self.assertIn("最終確認日", section)
        self.assertIn("テストVPS", section)
        self.assertIn("2024-06-20", section)

    def test_section_shows_unconfirmed_for_unknown_only(self):
        """verified_at がすべて unknown のプロバイダーは「未確認」と表示される。"""
        providers = [_make_provider("p1", "テストVPS")]
        evidence_list = [_make_evidence("p1", "f1", "v1", verified_at="unknown")]
        lines = generate_docs.generate_evidence_verified_at_section(providers, evidence_list)
        section = "\n".join(lines)
        self.assertIn("未確認", section)

    def test_comparison_table_includes_verified_at_section(self):
        """generate_comparison_table の出力に最終確認日セクションが含まれる。"""
        providers = [_make_provider("p1", "P1")]
        features = [_make_feature("f1", "項目1")]
        evidence_list = [_make_evidence("p1", "f1", "val", verified_at="2024-06-01")]
        evidence_map = generate_docs.build_evidence_map(evidence_list)
        md = generate_docs.generate_comparison_table(
            providers, features, evidence_map,
            category_order=_DEFAULT_CATEGORY_ORDER,
            category_labels=_DEFAULT_CATEGORY_LABELS,
            evidence_list=evidence_list,
        )
        self.assertIn("## 最終確認日", md)
        self.assertIn("2024-06-01", md)


class TestGenerateUseCasesPage(unittest.TestCase):

    def _generate(self, providers, features, evidence_list=None):
        evidence_map = generate_docs.build_evidence_map(evidence_list or [])
        return generate_docs.generate_use_cases_page(providers, features, evidence_map)

    def test_header_and_auto_gen_notice(self):
        """生成された Markdown に見出しと自動生成注記が含まれる。"""
        providers = [_make_provider()]
        features = [_make_feature("min_price_jpy", "最低月額料金（円）", category="PRICE", ftype="number")]
        md = self._generate(providers, features)
        self.assertIn("# 用途別 VPS 比較", md)
        self.assertIn("自動生成", md)

    def test_all_use_case_sections_present(self):
        """全用途のセクション見出しが出力される。"""
        providers = [_make_provider()]
        features = []
        md = self._generate(providers, features)
        for uc in generate_docs.USE_CASES:
            self.assertIn(f"## {uc['label']}", md)

    def test_known_feature_id_renders_in_table(self):
        """USE_CASES に含まれる feature_id が evidence 付きで表示される。"""
        providers = [_make_provider("prov-a", "ProvA")]
        features = [_make_feature("min_price_jpy", "最低月額料金（円）", category="PRICE", ftype="number")]
        evidence = [_make_evidence("prov-a", "min_price_jpy", 500)]
        md = self._generate(providers, features, evidence)
        self.assertIn("最低月額料金（円）", md)
        self.assertIn("500", md)

    def test_unknown_feature_id_shows_unknown_label(self):
        """evidence がない場合は UNKNOWN_LABEL が表示される。"""
        providers = [_make_provider("prov-a", "ProvA")]
        features = [_make_feature("min_price_jpy", "最低月額料金（円）", category="PRICE", ftype="number")]
        md = self._generate(providers, features, [])
        self.assertIn(generate_docs.UNKNOWN_LABEL, md)

    def test_feature_not_in_features_list_is_skipped(self):
        """features リストに存在しない feature_id はスキップされる。"""
        providers = [_make_provider()]
        # features に何も渡さない → USE_CASES の全 feature_id が feature_index に存在しない
        md = self._generate(providers, [])
        self.assertIn("（対応する比較項目がありません）", md)

    def test_legend_section_included(self):
        """凡例セクションが含まれる。"""
        providers = [_make_provider()]
        features = []
        md = self._generate(providers, features)
        self.assertIn("## 凡例", md)
        self.assertIn("対応あり", md)
        self.assertIn("非対応", md)

    def test_boolean_true_displays_check(self):
        """boolean: true は ✅ として表示される。"""
        providers = [_make_provider("prov-a", "ProvA")]
        # api_available は automation 用途の USE_CASES に含まれる
        features = [_make_feature("api_available", "REST API", category="automation", ftype="boolean")]
        evidence = [_make_evidence("prov-a", "api_available", True)]
        md = self._generate(providers, features, evidence)
        self.assertIn("✅", md)

    def test_provider_name_appears_in_header(self):
        """プロバイダー名がテーブルヘッダーに含まれる。"""
        providers = [_make_provider("p1", "MyVPS")]
        features = [_make_feature("api_available", "REST API", category="automation", ftype="boolean")]
        md = self._generate(providers, features)
        self.assertIn("MyVPS", md)


class TestFormatComparisonCell(unittest.TestCase):
    """format_comparison_cell のセル出力フォーマットを検証する。"""

    def test_value_only(self):
        """source_url と verified_at が unknown の場合は値のみ返す。"""
        entry = _make_evidence("p1", "f1", "460")
        result = generate_docs.format_comparison_cell(entry, "string")
        self.assertEqual(result, "460")

    def test_value_with_source_url(self):
        """source_url がある場合は値とリンクをスペースで結合する。"""
        entry = _make_evidence("p1", "f1", "460", source_url="https://example.com")
        result = generate_docs.format_comparison_cell(entry, "string")
        self.assertEqual(result, "460 [公式](https://example.com)")

    def test_value_with_verified_at(self):
        """verified_at がある場合は <br> で改行して確認日を追加する。"""
        entry = _make_evidence("p1", "f1", "460", verified_at="2026-07-03")
        result = generate_docs.format_comparison_cell(entry, "string")
        self.assertEqual(result, "460<br>(2026-07-03)")

    def test_value_with_source_url_and_verified_at(self):
        """source_url と verified_at がある場合は値・リンクを1行目、確認日を2行目に表示する。"""
        entry = _make_evidence("p1", "f1", "460",
                               source_url="https://example.com", verified_at="2026-07-03")
        result = generate_docs.format_comparison_cell(entry, "string")
        self.assertEqual(result, "460 [公式](https://example.com)<br>(2026-07-03)")

    def test_boolean_true_with_verified_at(self):
        """boolean true は ✅ で表示され、confirmed_at は <br> で改行される。"""
        entry = _make_evidence("p1", "f1", True, verified_at="2026-07-03")
        result = generate_docs.format_comparison_cell(entry, "boolean")
        self.assertEqual(result, "✅<br>(2026-07-03)")

    def test_unknown_verified_at_no_br(self):
        """verified_at が unknown の場合は <br> を追加しない。"""
        entry = _make_evidence("p1", "f1", "460", verified_at="unknown")
        result = generate_docs.format_comparison_cell(entry, "string")
        self.assertNotIn("<br>", result)
        self.assertNotIn("unknown", result)


class TestGenerateUpdateCandidatesPage(unittest.TestCase):

    def test_prioritized_unknown_sections(self):
        """unknown 項目が優先度付きで整理され、次の調査対象と確認困難項目が分離される。"""
        providers = [
            {
                "id": "p1",
                "name": "Provider A",
                "official_urls": {},
            },
            {
                "id": "p2",
                "name": "Provider B",
                "official_urls": {},
            },
        ]
        features = [
            _make_feature("min_price_jpy", "最低月額料金（円）", category="PRICE", ftype="number"),
            _make_feature("api_available", "REST API", category="OPS", ftype="boolean"),
        ]
        evidence_list = [
            {
                "provider_id": "p1",
                "feature_id": "min_price_jpy",
                "value": 500,
                "source_type": "official",
                "source_url": "https://example.com/pricing",
                "verified_at": "2026-07-01",
                "verification_status": "verified",
            },
            {
                "provider_id": "p1",
                "feature_id": "api_available",
                "value": "unknown",
                "source_type": "unknown",
                "source_url": "unknown",
                "verified_at": "unknown",
                "verification_status": "unknown",
            },
            {
                "provider_id": "p2",
                "feature_id": "api_available",
                "value": "unknown",
                "source_type": "unknown",
                "source_url": "unknown",
                "verified_at": "unknown",
                "verification_status": "unknown",
            },
        ]
        category_labels = {
            "PRICE": "料金",
            "OPS": "API / CLI / Terraform",
        }

        md = generate_docs.generate_update_candidates_page(
            providers, features, evidence_list, category_labels
        )

        self.assertIn("## カテゴリ別 unknown 集計", md)
        self.assertIn("| 高 | 料金 | 1 / 2 |", md)
        self.assertIn("| 料金 | 最低月額料金（円） | 1 / 2 | 1 / 2 |", md)
        self.assertIn("| 中 | API / CLI / Terraform | REST API |", md)
        self.assertNotIn("automation", md)
        self.assertNotIn("datacenter", md)

    def test_keeps_official_url_update_table(self):
        """公式URL更新候補テーブルが出力され、Status 判定が維持される。"""
        providers = [
            {
                "id": "p1",
                "name": "Provider A",
                "official_urls": {
                    "top": {"url": "https://example.com", "verified_at": "2020-01-01"},
                    "pricing": {"url": "unknown", "verified_at": "unknown"},
                    "specs": {"url": "unknown", "verified_at": "unknown"},
                    "support": {"url": "unknown", "verified_at": "unknown"},
                    "terms": {"url": "unknown", "verified_at": "unknown"},
                },
            }
        ]
        features = [_make_feature("f1", "項目", category="PRICE")]
        evidence_list = []

        md = generate_docs.generate_update_candidates_page(
            providers, features, evidence_list, {"PRICE": "料金"}, today=date(2026, 7, 8)
        )

        self.assertIn("## 公式URL更新候補", md)
        self.assertIn("| Provider A | top | https://example.com | 2020-01-01 | STALE |", md)


if __name__ == "__main__":
    unittest.main()
