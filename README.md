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
│   ├── validate.py
│   ├── generate_docs.py
│   └── check_links.py
├── docs/                  # 自動生成されたMarkdownドキュメント（手動編集不可）
│   ├── comparison.md      # プロバイダー比較テーブル
│   ├── providers.md       # プロバイダー詳細一覧
│   └── update_candidates.md # URL更新候補一覧
└── .github/workflows/
    ├── validate.yml       # PR時に自動検証を実行するワークフロー
    └── check-links.yml    # 手動でリンクチェックを実行するワークフロー
```

## クイックスタート

```bash
# 依存パッケージのインストール
pip install pyyaml

# 単体テストの実行
python -m unittest discover

# YAMLデータの検証
python scripts/validate.py

# 公式URLリンクチェック
python scripts/check_links.py

# Markdownドキュメントの生成
python scripts/generate_docs.py
```

## データの更新方法

1. 該当するYAMLファイル（`providers.yml` / `features.yml` / `evidence.yml` / `benchmarks.yml`）を編集します。
2. `evidence.yml` の変更には必ず `source_type`・`source_url`・`verified_at`・`verification_status` を記載してください（詳細は下記「Evidence管理ルール」参照）。
3. `python scripts/validate.py` でエラーがないことを確認します。
4. `python scripts/generate_docs.py` で `docs/` 以下を更新します。
5. プルリクエストを作成します。CIが自動でYAMLを検証します。

## 生成ドキュメントの運用ルール

`docs/` 以下のMarkdownファイルは `scripts/generate_docs.py` により自動生成される **生成物** です。手動で編集しないでください。

### PRを作成する前に必ず実行してください

YAMLファイル（`providers.yml` / `features.yml` / `evidence.yml` / `benchmarks.yml`）または `scripts/generate_docs.py` を変更した場合は、必ず以下を実行してから `docs/` の変更をコミットしてください。

```bash
python scripts/generate_docs.py
```

### CIによる差分検出

PRのCIでは `generate_docs.py` を実行し、`git diff --exit-code` で生成物の差分を検出します。  
**`docs/` の更新がコミットされていない場合、CIが失敗します。**

差分が検出された場合は、ローカルで `python scripts/generate_docs.py` を実行して生成物を更新し、コミットしてからプッシュしてください。

## providers.yml 記述ルール

`providers.yml` に Provider を追加・編集する際は、以下のルールに従ってください。

### 必須フィールド

各 Provider には以下のフィールドが必須です。

| フィールド | 説明 |
| --- | --- |
| `id` | Provider の一意識別子 |
| `name` | Provider の表示名 |
| `company` | 運営会社名 |
| `url` | 公式サイトURL |
| `official_urls` | 公式URL一覧（辞書形式） |
| `datacenter_locations` | データセンター所在地（リスト） |
| `support_language` | サポート言語（リスト） |

### id

- 英小文字・数字・ハイフン（`-`）のみ使用できます（例: `my-vps`, `example-provider`）
- リポジトリ内で重複不可

### name

- 空文字は不可

### url

- `https://` で始まる有効なURLであること
- `unknown` は不可

### official_urls

`official_urls` は辞書形式で、以下のキーが必須です。各値は `url` と `verified_at` を持つ辞書です。

| キー | 説明 |
| --- | --- |
| `top` | 公式サイトのトップページ |
| `pricing` | 料金ページ |
| `specs` | 仕様ページ |
| `support` | サポートページ |
| `terms` | 利用規約ページ |

各エントリの `url` は `https://` で始まる有効なURLまたは `unknown` を指定します。

```yaml
official_urls:
  top:
    url: https://example.com/
    verified_at: "2024-01-01"  # YYYY-MM-DD 形式 または unknown
  pricing:
    url: https://example.com/pricing/
    verified_at: unknown
  specs:
    url: unknown
    verified_at: unknown
  support:
    url: unknown
    verified_at: unknown
  terms:
    url: https://example.com/terms/
    verified_at: unknown
```

## validate.py 検証内容

`scripts/validate.py` は以下の検証を行います。

### providers.yml

| 対象 | 検証内容 |
| --- | --- |
| `id` | 必須・英小文字/数字/ハイフンのみ・リポジトリ内で一意（重複不可） |
| `name` | 必須・空文字不可 |
| `url` | 必須・`https://` で始まる有効なURL |
| `official_urls` | 必須・辞書形式・各キーの `url` は `https://` で始まるURLまたは `unknown` |
| `official_urls` の各キー | `top` / `pricing` / `specs` / `support` / `terms` が存在すること |
| `official_urls` の各エントリ | `url` と `verified_at` が存在すること |
| `official_urls` 内の URL | 同一プロバイダー内で重複がある場合は警告（`unknown` は対象外） |
| `aliases` | 同一プロバイダー内で重複不可・他プロバイダーの `id` と衝突不可 |

### features.yml

| 対象 | 検証内容 |
| --- | --- |
| `id` | 必須・リポジトリ内で一意 |
| `category` | 必須・定義済みカテゴリ値のみ |
| `type` | 必須・`number` / `boolean` / `string` のいずれか |

### evidence.yml

| 対象 | 検証内容 |
| --- | --- |
| `provider_id` | 必須・`providers.yml` に存在すること |
| `feature_id` | 必須・`features.yml` に存在すること |
| `(provider_id, feature_id)` | 組み合わせ重複不可 |
| `source_type` | 必須・`official` / `benchmark` / `manual` / `community` / `unknown` のいずれか |
| `source_url` | 必須・`https://` で始まるURLまたは `unknown` |
| `verified_at` | 必須・`YYYY-MM-DD` 形式または `unknown` |
| `verification_status` | 必須・`verified` / `unverified` / `unknown` のいずれか |

### benchmarks.yml

| 対象 | 検証内容 |
| --- | --- |
| `provider_id` | 必須・`providers.yml` に存在すること |
| `tests` の各エントリ | `metric` / `value` / `tool` / `measured_at` / `measured_by` が存在すること |

## 公式URLリンクチェック

`scripts/check_links.py` は `providers.yml` の `official_urls` を順に確認し、HTTPステータスを検証します。

- 成功: `2xx` / `3xx`
- 失敗: `4xx` / `5xx` / タイムアウト / 接続エラー
- `url: unknown` はチェック対象外

実行方法:

```bash
python scripts/check_links.py
```

GitHub Actions で手動実行する場合:

1. GitHub の **Actions** タブを開く
2. **Check Links（手動実行）** ワークフローを選択する
3. **Run workflow** をクリックして実行する

失敗時は、以下のように `provider_id` と `url` が出力されます。

```text
[FAIL] provider_id=example-vps url=https://example.com/xxx (status=404)
```

一時的な外部要因で失敗する場合があるため、時間を置いて再実行し、それでも失敗する場合は `providers.yml` のURL変更有無を確認してください。

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
