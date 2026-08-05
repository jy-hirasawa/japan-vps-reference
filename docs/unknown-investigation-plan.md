# 「不明」項目の整理方針

このドキュメントは Issue #100 向けに、`docs/comparison.md` の「不明」項目をどのように棚卸し・分割調査するかを整理したものです。

`docs/comparison.md` は `scripts/generate_docs.py` により自動生成されるため、直接編集しません。集計対象の正データは `features.yml`・`providers.yml`・`evidence.yml` です。

## 生成元データと生成処理

- 比較項目定義: `features.yml`
- プロバイダー定義: `providers.yml`
- 比較値と根拠: `evidence.yml`
- 生成スクリプト: `scripts/generate_docs.py`
- 自動生成される比較関連ドキュメント:
  - `docs/comparison.md`
  - `docs/update_candidates.md`
  - `docs/use-cases.md`
  - `docs/providers.md`

`scripts/generate_docs.py` は `evidence.yml` の `value: unknown` を「不明」として整形し、`docs/update_candidates.md` ではカテゴリ別・Provider別の unknown 件数も自動集計しています。

## 現状集計（2026-08-05 時点）

### unknown 総件数

- 総件数: **244**

### カテゴリ別件数

`docs/update_candidates.md` の自動集計結果を基準とします。

| 優先度 | カテゴリ | unknown / 総セル数 | unknown率 |
| --- | --- | --- | --- |
| 高 | 基本情報 | 24 / 30 | 80% |
| 高 | バックアップ / イメージ保存 | 23 / 50 | 46% |
| 高 | ネットワーク | 21 / 55 | 38% |
| 高 | OS / テンプレート | 11 / 30 | 36% |
| 高 | ディスク / NVMe / スナップショット / バックアップ | 11 / 55 | 20% |
| 高 | サポート / SLA | 8 / 65 | 12% |
| 高 | 料金 | 2 / 45 | 4% |
| 高 | CPU / メモリ | 0 / 10 | 0% |
| 中 | API / CLI / Terraform | 52 / 60 | 86% |
| 中 | データセンター / リージョン | 50 / 60 | 83% |
| 中 | セキュリティ | 42 / 60 | 70% |

### Provider別件数

| Provider | unknown件数 |
| --- | --- |
| WebARENA Indigo | 58 |
| Xserver VPS | 55 |
| KAGOYA CLOUD VPS | 51 |
| さくらのVPS | 43 |
| ConoHa VPS | 37 |

## unknown の暫定分類

現行スキーマでは `unknown` の理由を明示的には保持していません。そのため、親Issue段階では以下の暫定ルールで棚卸しします。

| 暫定分類 | 判定条件 |
| --- | --- |
| 未調査 | `value: unknown` かつ `source_type/source_url/verified_at/verification_status` がすべて `unknown` |
| 確認できず | `value: unknown` だが、公式URLまたは確認日などの調査痕跡がある |
| 非対応 | `boolean` なら `false`、文字列系なら `"-"` を使用済み |
| 対象外 | 現状は値として専用表現なし。必要に応じて今後追加検討 |
| 対応 | `true` または具体値が入っている状態 |

### 暫定分類の集計

- 未調査: **242**
- 確認できず: **2**

「確認できず」に該当する既存例:

| カテゴリ | 項目 | Provider | 根拠 |
| --- | --- | --- | --- |
| ディスク / NVMe / スナップショット / バックアップ | オブジェクトストレージ連携 | Xserver VPS | 公式サイトを調査したが連携案内を確認できず |
| ディスク / NVMe / スナップショット / バックアップ | オブジェクトストレージ連携 | KAGOYA CLOUD VPS | 公式サイトを調査したが連携案内を確認できず |

## 優先して対応すべきカテゴリ

Issue #100 の優先案と既存 unknown 件数を踏まえ、子Issue化の優先順は以下とします。

1. 基本情報
2. ネットワーク
3. バックアップ / イメージ保存
4. ローカルネットワーク関連（ネットワーク内の重点項目）
5. 可用性・障害対応（`SUPPORT` / `datacenter` の一部）
6. サポート
7. OS / テンプレート
8. セキュリティ
9. API / CLI / Terraform
10. データセンター / リージョン

補足:

- `API / CLI / Terraform`・`データセンター / リージョン`・`セキュリティ` は件数が多い一方で、公式情報で確認しづらい項目を多く含みます。
- そのため、件数のみでなく「比較上の重要度」と「既に公式URL付き根拠がある項目から着手できるか」を優先基準にします。
- `docs/update_candidates.md` の「次に調査すべき項目（優先度: 高）」を各子Issueの対象選定に利用します。

## 子Issue案

### 1. 基本情報カテゴリの「不明」項目を調査する

- 対象カテゴリ: `BASIC`
- 主な対象項目: `root_access`, `linux_support`, `windows_official`, `console_vnc`, `startup_script`, `cloud_init`
- 目的: 比較時の前提となる基本提供範囲を先に固める

### 2. ネットワークカテゴリの「不明」項目を調査する

- 対象カテゴリ: `NETWORK`
- 主な対象項目: `private_network`, `local_network`, `vlan`, `floating_ip`, `load_balancer`, `additional_ipv4`, `bandwidth_gbps`
- 目的: 比較需要の高い接続性・構成要素を整理する

### 3. バックアップ / イメージ保存カテゴリの「不明」項目を調査する

- 対象カテゴリ: `BACKUP`
- 主な対象項目: `backup_schedule`, `backup_retention_period`, `backup_generations`, `restore_from_backup`, `backup_encryption`, `backup_to_object_storage`, `cross_region_backup`, `backup_billing`
- 目的: DR・復旧性の比較に必要な項目を重点調査する

### 4. ディスク / スナップショット関連の「不明」項目を調査する

- 対象カテゴリ: `STORAGE`
- 主な対象項目: `nvme_explicit`, `additional_disk`, `disk_expansion`, `auto_snapshot`, `object_storage_integration`
- 目的: `BACKUP` と近いが、ストレージ機能として別レビューしやすくする

### 5. サポート / SLA と可用性関連の「不明」項目を調査する

- 対象カテゴリ: `SUPPORT`
- 関連カテゴリ: `datacenter`
- 主な対象項目: `phone_support`, `chat_support`, `corporate_support`, `sla_document_url`, `sla_uptime_percent`, `status_page`, `incident_page`
- 目的: 契約・障害時対応・稼働率の比較情報を優先的に整備する

### 6. OS / テンプレートカテゴリの「不明」項目を調査する

- 対象カテゴリ: `OS_TEMPLATE`
- 主な対象項目: `docker_template`, `kusanagi_template`, `ai_template`, `custom_iso`
- 目的: 初期構築容易性に関する比較情報を整理する

### 7. セキュリティカテゴリの「不明」項目を調査する

- 対象カテゴリ: `SECURITY`
- 主な対象項目: `ssh_key`, `iam_rbac`, `firewall_feature`, `ddos_protection`, `audit_log`, `isms`, `soc2`, `pci_dss`
- 目的: VPS機能と事業者/データセンター認証を混同しない形で整理する

### 8. API / CLI / Terraform カテゴリの「不明」項目を調査する

- 対象カテゴリ: `automation`
- 主な対象項目: `cli_available`, `terraform_provider`, `pulumi_support`, `ansible_support`, `metadata_service`, `webhook`, `sdk_go`, `sdk_python`, `sdk_nodejs`
- 目的: 自動化用途の比較に必要な項目をまとめて調査する

### 9. 「不明」状態のデータ表現を見直す

- 対象ファイル: `evidence.yml`, `scripts/validate.py`, `scripts/generate_docs.py`, 関連テスト
- 目的: `unknown` の理由を `value` とは別に保持し、`未調査` と `確認できず` を区別できるようにする

### 10. 「不明」項目一覧の自動生成機能を拡張する

- 対象ファイル: `scripts/generate_docs.py`, `docs/update_candidates.md`
- 目的: カテゴリ別件数だけでなく、項目 × Provider の棚卸し一覧と調査状態を自動出力できるようにする

## 最小限のデータ構造案

既存の `value` / `source_type` / `source_url` / `verified_at` / `verification_status` は維持し、`evidence.yml` の各エントリに補助フィールドを追加する案を推奨します。

```yaml
- provider_id: example-vps
  feature_id: example-feature
  value: unknown
  research_status: unresearched
  applicability_status: applicable
  source_type: unknown
  source_url: unknown
  verified_at: unknown
  verification_status: unknown
```

### 追加候補フィールド

| フィールド | 値候補 | 用途 |
| --- | --- | --- |
| `research_status` | `unresearched` / `checked_not_found` / `confirmed_supported` / `confirmed_unsupported` / `not_applicable` | 調査状況を保持する |
| `applicability_status` | `applicable` / `not_applicable` / `unknown` | 比較対象かどうかを明示する |

### この案の意図

- `value` の型互換性を維持できる
- `false` / `"-"` による「確認済み非対応」の既存表現を壊さない
- `unknown` であっても「未調査」と「確認できず」を区別できる
- 生成スクリプト側では `research_status` を使って棚卸し一覧を作れる

## 調査ルール

- 根拠として使う情報源は公式サイト・公式料金ページ・公式仕様ページ・公式マニュアル・公式FAQ・公式サポート情報・公式利用規約・公式のお知らせに限定する
- ブログ・比較サイト・SNS・個人記事は比較表の根拠に使わない
- 各確認結果には `source_url` と `verified_at` を記録する
- 判断に迷う場合は `unknown` のまま残し、必要に応じて `notes` に補足する
- 「見つからない」ことだけを理由に `false` / `"-"` を入れない

## 今後の更新フロー

1. 子Issue単位で対象カテゴリと対象Providerを固定する
2. `evidence.yml` を更新する
3. `python scripts/validate.py` を実行する
4. `python scripts/generate_docs.py` を実行する
5. `docs/comparison.md` と `docs/update_candidates.md` の差分を確認する

