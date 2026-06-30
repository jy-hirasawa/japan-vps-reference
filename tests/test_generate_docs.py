"""
tests/test_generate_docs.py — scripts/generate_docs.py の単体テスト
"""

import sys
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
