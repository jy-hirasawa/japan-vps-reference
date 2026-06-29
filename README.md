# 日本の VPS 比較リファレンス

日本国内の国内VPS5社（さくらのVPS・ConoHa VPS・Xserver VPS・WebARENA Indigo・KAGOYA CLOUD VPS）について、公式情報を根拠としたデータを整備・比較するリポジトリです。

## 公式情報優先ポリシー

このリポジトリでは **公式情報優先（Official-First）** ポリシーを採用しています。

- **事実のみを記載します。** 推測・憶測・非公式の口コミは掲載しません。
- **不明な情報は `"unknown"` と明示します。** 空欄や憶測で補完することを禁止しています。
- **根拠URLと確認日を記録します。** `evidence.yml` の各エントリには `source_url`（公式URL）と `verified_at`（確認日）を必ず記載します。
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
│   ├── providers.md       # プロバイダー詳細一覧
│   └── update_candidates.md # URL更新候補一覧
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
2. `evidence.yml` の変更には必ず `source_type`・`source_url`・`verified_at`・`verification_status` を記載してください（詳細は下記「Evidence管理ルール」参照）。
3. `python scripts/validate.py` でエラーがないことを確認します。
4. `python scripts/generate_docs.py` で `docs/` 以下を更新します。
5. プルリクエストを作成します。CIが自動でYAMLを検証します。

## Evidence 管理ルール

`evidence.yml` の各エントリには、値の根拠と検証状態を示す以下のメタデータを必ず記載してください。

### 必須フィールド

| フィールド | 説明 | 許容値 |
| --- | --- | --- |
| `source_type` | 情報源の種別 | `official` / `benchmark` / `manual` / `community` / `unknown` |
| `source_url` | 情報源のURL | `https://...` 形式のURL または `unknown` |
| `verified_at` | 情報を確認した日付 | `YYYY-MM-DD` 形式 または `unknown` |
| `verification_status` | 検証状態 | `verified` / `unverified` / `unknown` |

### 任意フィールド

| フィールド | 説明 |
| --- | --- |
| `notes` | 補足情報（制限事項・条件・注意事項など） |

### source_type の選択基準

- `official` — プロバイダーの公式サイト・公式ドキュメントを根拠とする場合
- `benchmark` — ベンチマーク測定結果を根拠とする場合
- `manual` — 実際に操作・確認した結果を根拠とする場合
- `community` — コミュニティ情報（ブログ・フォーラム等）を根拠とする場合（推奨しない）
- `unknown` — 情報源が不明な場合

### verification_status の選択基準

- `verified` — `source_url` のページで内容を確認済みの場合
- `unverified` — 情報源はあるが内容未確認の場合
- `unknown` — 検証状態が不明な場合（`source_type: unknown` のエントリ等）

### 記載例

```yaml
# 公式サイトで確認済みの場合
- provider_id: example-vps
  feature_id: min_price_jpy
  value: 500
  source_type: official
  source_url: https://example.com/pricing/
  verified_at: "2024-01-01"
  verification_status: verified

# 情報が未確認の場合
- provider_id: example-vps
  feature_id: bandwidth_gbps
  value: unknown
  source_type: unknown
  source_url: unknown
  verified_at: unknown
  verification_status: unknown
```

## 比較テーブル

生成済みドキュメント:

- [`docs/comparison.md`](docs/comparison.md) — VPS比較テーブル
- [`docs/providers.md`](docs/providers.md) — プロバイダー詳細一覧
- [`docs/update_candidates.md`](docs/update_candidates.md) — URL更新候補一覧

## ライセンス

データは [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.ja) で提供します。
