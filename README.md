# 日本の VPS 比較リファレンス

日本国内の国内VPS5社（さくらのVPS・ConoHa VPS・Xserver VPS・WebARENA Indigo・KAGOYA CLOUD VPS）について、公式情報を根拠としたデータを整備・比較するリポジトリです。

## 公式情報優先ポリシー

このリポジトリでは **公式情報優先（Official-First）** ポリシーを採用しています。

- **事実のみを記載します。** 推測・憶測・非公式の口コミは掲載しません。
- **不明な情報は `"unknown"` と明示します。** 空欄や憶測で補完することを禁止しています。
- **根拠URLと取得日を記録します。** `evidence.yml` の各エントリには `source`（公式URL）と `retrieved`（取得日）を必ず記載します。
- **情報が古くなった場合は更新します。** 定期的に公式ページを確認し、差異があれば修正PRを作成してください。

## リポジトリ構成

```
.
├── providers.yml          # VPSプロバイダー一覧（会社名・所在地等）
├── features.yml           # 比較項目の定義（型・説明）
├── evidence.yml           # プロバイダーごとの機能・仕様データ（根拠URL付き）
├── benchmarks.yml         # ベンチマーク測定結果
├── scripts/
│   ├── validate.py        # 必須フィールド検証スクリプト
│   └── generate_docs.py   # Markdown比較テーブル生成スクリプト
├── docs/                  # 自動生成されたMarkdownドキュメント（手動編集不可）
│   ├── comparison.md      # プロバイダー比較テーブル
│   └── providers.md       # プロバイダー詳細一覧
└── .github/workflows/
    └── validate.yml       # PR時に自動検証を実行するワークフロー
```

## クイックスタート

```bash
# 依存パッケージのインストール
pip install pyyaml

# YAMLデータの検証
python scripts/validate.py

# Markdownドキュメントの生成
python scripts/generate_docs.py
```

## データの更新方法

1. 該当するYAMLファイル（`providers.yml` / `features.yml` / `evidence.yml` / `benchmarks.yml`）を編集します。
2. `evidence.yml` の変更には必ず `source`（公式URL）と `retrieved`（取得日 `YYYY-MM-DD`）を記載してください。
3. `python scripts/validate.py` でエラーがないことを確認します。
4. `python scripts/generate_docs.py` で `docs/` 以下を更新します。
5. プルリクエストを作成します。CIが自動でYAMLを検証します。

## 比較テーブル

生成済みの比較テーブルは [`docs/comparison.md`](docs/comparison.md) を参照してください。

## ライセンス

データは [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.ja) で提供します。
