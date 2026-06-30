"""
tests/test_validate.py — scripts/validate.py の単体テスト
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import validate


def _make_provider(**kwargs) -> dict:
    """最低限の有効な provider データを生成するヘルパー。"""
    base = {
        "id": "test-provider",
        "name": "Test Provider",
        "company": "Test Co",
        "url": "https://test.example.com",
        "official_urls": {
            "top":     {"url": "https://test.example.com",         "verified_at": "2024-01-01"},
            "pricing": {"url": "https://test.example.com/pricing", "verified_at": "2024-01-01"},
            "specs":   {"url": "https://test.example.com/specs",   "verified_at": "2024-01-01"},
            "support": {"url": "https://test.example.com/support", "verified_at": "2024-01-01"},
            "terms":   {"url": "https://test.example.com/terms",   "verified_at": "2024-01-01"},
        },
        "datacenter_locations": ["Tokyo"],
        "support_language": ["ja"],
    }
    base.update(kwargs)
    return base


class TestValidateProviders(unittest.TestCase):

    def setUp(self):
        validate.errors.clear()
        validate.warnings.clear()

    # ------------------------------------------------------------------
    # 正常系
    # ------------------------------------------------------------------

    def test_valid_provider_no_errors(self):
        """正常な provider データはエラー・警告が発生しない。"""
        data = {"providers": [_make_provider()]}
        validate.validate_providers(data)
        self.assertEqual(validate.errors, [])
        self.assertEqual(validate.warnings, [])

    # ------------------------------------------------------------------
    # 必須フィールド不足
    # ------------------------------------------------------------------

    def test_missing_required_fields(self):
        """必須フィールドが欠けている場合にエラーが発生する。"""
        data = {"providers": [{"id": "test-provider"}]}
        validate.validate_providers(data)
        error_text = "\n".join(validate.errors)
        for field in ["name", "company", "url", "official_urls",
                      "datacenter_locations", "support_language"]:
            self.assertIn(field, error_text, f"必須フィールド '{field}' が検出されなかった")

    # ------------------------------------------------------------------
    # 不正な id
    # ------------------------------------------------------------------

    def test_invalid_id_uppercase(self):
        """大文字を含む id はエラーになる。"""
        data = {"providers": [_make_provider(id="Invalid-ID")]}
        validate.validate_providers(data)
        self.assertTrue(
            any("Invalid-ID" in e for e in validate.errors),
            "不正な id が検出されなかった",
        )

    def test_invalid_id_underscore(self):
        """アンダースコアを含む id はエラーになる。"""
        data = {"providers": [_make_provider(id="invalid_id")]}
        validate.validate_providers(data)
        self.assertTrue(
            any("invalid_id" in e for e in validate.errors),
            "アンダースコアを含む id が検出されなかった",
        )

    def test_valid_id_hyphen(self):
        """英小文字・数字・ハイフンのみの id はエラーにならない。"""
        data = {"providers": [_make_provider(id="valid-id-123")]}
        validate.validate_providers(data)
        self.assertEqual(validate.errors, [])

    # ------------------------------------------------------------------
    # provider_id の重複
    # ------------------------------------------------------------------

    def test_duplicate_provider_id(self):
        """同じ id を持つ provider が複数存在する場合にエラーになる。"""
        p = _make_provider(id="dup-id")
        # id を変えずに 2 件登録
        data = {"providers": [p, dict(p)]}
        validate.validate_providers(data)
        self.assertTrue(
            any("重複" in e for e in validate.errors),
            "provider_id の重複が検出されなかった",
        )

    # ------------------------------------------------------------------
    # official_urls の重複 URL → Warning
    # ------------------------------------------------------------------

    def test_duplicate_official_url_is_warning(self):
        """official_urls 内に同じ URL が複数存在する場合は Warning になる。"""
        dup_url = "https://test.example.com/dup"
        data = {
            "providers": [
                _make_provider(
                    official_urls={
                        "top":     {"url": dup_url,                               "verified_at": "2024-01-01"},
                        "pricing": {"url": dup_url,                               "verified_at": "2024-01-01"},
                        "specs":   {"url": "https://test.example.com/specs",     "verified_at": "2024-01-01"},
                        "support": {"url": "https://test.example.com/support",   "verified_at": "2024-01-01"},
                        "terms":   {"url": "https://test.example.com/terms",     "verified_at": "2024-01-01"},
                    }
                )
            ]
        }
        validate.validate_providers(data)
        self.assertEqual(validate.errors, [], "URL重複はエラーではなく Warning であるべき")
        self.assertTrue(
            any("重複" in w for w in validate.warnings),
            "official_urls の URL 重複が Warning として検出されなかった",
        )

    # ------------------------------------------------------------------
    # aliases の重複
    # ------------------------------------------------------------------

    def test_duplicate_aliases(self):
        """aliases リスト内に重複エントリがある場合にエラーになる。"""
        data = {
            "providers": [
                _make_provider(aliases=["alias-one", "alias-one"])
            ]
        }
        validate.validate_providers(data)
        self.assertTrue(
            any("aliases" in e and "重複" in e for e in validate.errors),
            "aliases の重複が検出されなかった",
        )

    # ------------------------------------------------------------------
    # aliases と provider_id の衝突
    # ------------------------------------------------------------------

    def test_alias_collides_with_provider_id(self):
        """aliases の値が別 provider の id と衝突する場合にエラーになる。"""
        data = {
            "providers": [
                _make_provider(id="provider-a", aliases=["provider-b"]),
                _make_provider(
                    id="provider-b",
                    url="https://b.example.com",
                    official_urls={
                        "top":     {"url": "https://b.example.com",         "verified_at": "2024-01-01"},
                        "pricing": {"url": "https://b.example.com/pricing", "verified_at": "2024-01-01"},
                        "specs":   {"url": "https://b.example.com/specs",   "verified_at": "2024-01-01"},
                        "support": {"url": "https://b.example.com/support", "verified_at": "2024-01-01"},
                        "terms":   {"url": "https://b.example.com/terms",   "verified_at": "2024-01-01"},
                    },
                ),
            ]
        }
        validate.validate_providers(data)
        self.assertTrue(
            any("衝突" in e for e in validate.errors),
            "alias と provider_id の衝突が検出されなかった",
        )


def _make_categories(ids: list[str] | None = None) -> list[dict]:
    """テスト用カテゴリリストを生成するヘルパー。"""
    all_cats = {
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
    target = ids if ids is not None else list(all_cats.keys())
    return [{"id": cid, "label": all_cats.get(cid, cid)} for cid in target]


def _make_feature(**kwargs) -> dict:
    """最低限の有効な feature データを生成するヘルパー。"""
    base = {
        "id": "test-feature",
        "category": "BASIC",
        "label": "テスト項目",
        "description": "テスト用の説明。",
        "type": "string",
    }
    base.update(kwargs)
    return base


def _make_features_data(features: list, categories: list | None = None) -> dict:
    """features と categories を持つ features.yml 相当のデータを生成するヘルパー。"""
    return {
        "categories": _make_categories() if categories is None else categories,
        "features": features,
    }


class TestValidateFeatures(unittest.TestCase):

    def setUp(self):
        validate.errors.clear()
        validate.warnings.clear()

    # ------------------------------------------------------------------
    # 正常系
    # ------------------------------------------------------------------

    def test_valid_feature_no_errors(self):
        """正常な feature データはエラーが発生しない。"""
        data = _make_features_data([_make_feature()])
        validate.validate_features(data)
        self.assertEqual(validate.errors, [])

    def test_valid_feature_all_types(self):
        """有効な type 値（number / boolean / string）はエラーにならない。"""
        for ftype in ("number", "boolean", "string"):
            validate.errors.clear()
            data = _make_features_data([_make_feature(id=f"feat-{ftype}", type=ftype)])
            validate.validate_features(data)
            self.assertEqual(validate.errors, [], f"type='{ftype}' でエラーが発生した")

    def test_valid_feature_all_categories(self):
        """features.yml で定義されたカテゴリはすべてエラーにならない。"""
        all_cat_ids = ["BASIC", "PRICE", "SPEC", "STORAGE", "NETWORK",
                       "SECURITY", "BACKUP", "OPS", "SUPPORT", "BENCH"]
        for i, cat in enumerate(all_cat_ids):
            validate.errors.clear()
            data = _make_features_data([_make_feature(id=f"feat-{i}", category=cat)])
            validate.validate_features(data)
            self.assertEqual(validate.errors, [], f"category='{cat}' でエラーが発生した")

    # ------------------------------------------------------------------
    # 必須フィールド不足
    # ------------------------------------------------------------------

    def test_missing_required_fields(self):
        """必須フィールドが欠けている場合にエラーが発生する。"""
        data = _make_features_data([{"id": "bare-feature"}])
        validate.validate_features(data)
        error_text = "\n".join(validate.errors)
        for field in ["category", "label", "description", "type"]:
            self.assertIn(field, error_text, f"必須フィールド '{field}' が検出されなかった")

    # ------------------------------------------------------------------
    # id の重複
    # ------------------------------------------------------------------

    def test_duplicate_feature_id(self):
        """同じ id を持つ feature が複数存在する場合にエラーになる。"""
        f = _make_feature(id="dup-feature")
        data = _make_features_data([f, dict(f)])
        validate.validate_features(data)
        self.assertTrue(
            any("重複" in e for e in validate.errors),
            "feature_id の重複が検出されなかった",
        )

    # ------------------------------------------------------------------
    # 不正な category
    # ------------------------------------------------------------------

    def test_invalid_category(self):
        """categories に定義されていないカテゴリを指定した場合にエラーになる。"""
        data = _make_features_data([_make_feature(category="INVALID_CATEGORY")])
        validate.validate_features(data)
        self.assertTrue(
            any("INVALID_CATEGORY" in e for e in validate.errors),
            "不正なカテゴリが検出されなかった",
        )

    # ------------------------------------------------------------------
    # categories セクションの検証
    # ------------------------------------------------------------------

    def test_categories_required_fields(self):
        """categories に必須フィールドが欠けている場合にエラーが発生する。"""
        data = _make_features_data(
            [],
            categories=[{"id": "BASIC"}],  # label が欠けている
        )
        validate.validate_features(data)
        error_text = "\n".join(validate.errors)
        self.assertIn("label", error_text, "categories の必須フィールド 'label' が検出されなかった")

    def test_duplicate_category_id(self):
        """categories に同じ id が重複している場合にエラーになる。"""
        data = _make_features_data(
            [],
            categories=[
                {"id": "BASIC", "label": "基本情報"},
                {"id": "BASIC", "label": "基本情報（重複）"},
            ],
        )
        validate.validate_features(data)
        self.assertTrue(
            any("重複" in e for e in validate.errors),
            "categories の id 重複が検出されなかった",
        )

    # ------------------------------------------------------------------
    # 不正な type
    # ------------------------------------------------------------------

    def test_invalid_type(self):
        """未定義の type を指定した場合にエラーになる。"""
        data = _make_features_data([_make_feature(type="integer")])
        validate.validate_features(data)
        self.assertTrue(
            any("integer" in e for e in validate.errors),
            "不正な type が検出されなかった",
        )

    # ------------------------------------------------------------------
    # id のフォーマット検証
    # ------------------------------------------------------------------

    def test_invalid_id_uppercase(self):
        """大文字を含む feature id はエラーになる。"""
        data = _make_features_data([_make_feature(id="Invalid-Feature")])
        validate.validate_features(data)
        self.assertTrue(
            any("Invalid-Feature" in e for e in validate.errors),
            "大文字を含む feature id が検出されなかった",
        )

    def test_invalid_id_special_chars(self):
        """英小文字・数字・ハイフン・アンダースコア以外の文字を含む id はエラーになる。"""
        data = _make_features_data([_make_feature(id="feat.special")])
        validate.validate_features(data)
        self.assertTrue(
            any("feat.special" in e for e in validate.errors),
            "不正な文字を含む feature id が検出されなかった",
        )

    def test_valid_id_underscore(self):
        """アンダースコアを含む feature id はエラーにならない。"""
        data = _make_features_data([_make_feature(id="my_feature_123")])
        validate.validate_features(data)
        self.assertEqual(validate.errors, [], "アンダースコアを含む feature id でエラーが発生した")

    def test_valid_id_hyphen(self):
        """ハイフンを含む feature id はエラーにならない。"""
        data = _make_features_data([_make_feature(id="my-feature-123")])
        validate.validate_features(data)
        self.assertEqual(validate.errors, [], "ハイフンを含む feature id でエラーが発生した")

    def test_empty_id(self):
        """空文字の feature id はエラーになる。"""
        data = _make_features_data([_make_feature(id="")])
        validate.validate_features(data)
        self.assertTrue(
            any("id が空文字" in e for e in validate.errors),
            "空文字の feature id が検出されなかった",
        )

    # ------------------------------------------------------------------
    # 空の label / category 検証
    # ------------------------------------------------------------------

    def test_empty_label(self):
        """空文字の label はエラーになる。"""
        data = _make_features_data([_make_feature(label="")])
        validate.validate_features(data)
        self.assertTrue(
            any("label が空文字" in e for e in validate.errors),
            "空文字の label が検出されなかった",
        )

    def test_empty_category(self):
        """空文字の category はエラーになる。"""
        data = _make_features_data([_make_feature(category="")])
        validate.validate_features(data)
        self.assertTrue(
            any("category が空文字" in e for e in validate.errors),
            "空文字の category が検出されなかった",
        )


if __name__ == "__main__":
    unittest.main()
