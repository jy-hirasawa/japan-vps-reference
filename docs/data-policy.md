# データポリシー

このドキュメントは `evidence.yml` で使用する値の表現ルールを定めます。
今後のデータ追加・更新時に解釈がブレないよう、Copilot を含むすべての編集者が参照してください。

## 基本方針

- **公式情報のみ記載する。** 推測・憶測・非公式の口コミは掲載しない。
- **不明な値は `unknown` と明示する。** 空欄や憶測で補完しない。
- **確認済みの「非対応」は `"-"` または `false` で表す。** `unknown` と混同しない。

## 値の表現ルール

| 値 | 型 | 意味 | 使用例 |
| --- | --- | --- | --- |
| `unknown` | string | 未確認・公式情報から判断できない | 公式ページに記載がない場合 |
| `"-"` | string | プランなし・非対応・該当なし（確認済み） | 時間課金非対応プランの時間単価 |
| `0` | number | 数値として 0（確認済み） | 初期費用なし（0円）の場合 |
| `false` | boolean | 機能として非対応（確認済み） | 時間課金に非対応の場合 |
| `true` | boolean | 機能として対応（確認済み） | IPv6 に対応している場合 |

### `unknown` と `"-"` の違い

- **`unknown`**: 情報が**不明**。公式ページで確認できなかったため、値を記載できない状態。
- **`"-"`**: 情報が**確認済みで非対応・該当なし**。公式ページで「このプランには該当しない」と確認できた状態。

例:
- 時間課金の価格が公式ページに掲載されていない → `unknown`
- 時間課金に対応していないことが公式ページで確認できた → `"-"` または `false`

### `0` と `false` の違い

- **`0`**: **number 型**の 0。「初期費用が 0 円」のように数値として 0 であることが確認済みの場合。
  - feature の `type: number` に対応する。
- **`false`**: **boolean 型**の非対応。機能の有無を示すフィールドで、非対応であることが確認済みの場合。
  - feature の `type: boolean` に対応する。

### `false` と `"-"` の違い

- **`false`**: boolean 型フィールド（`type: boolean`）で非対応を示す。
- **`"-"`**: string / number 型フィールド（`type: string` / `type: number`）で該当なし・非対応を示す。
  - 例: 時間課金に非対応のため時間単価が存在しない場合は `"-"` を使う（数値フィールドだが値が存在しないため）。

### 空欄について

`evidence.yml` の `value` フィールドは空欄にしない。値が不明な場合は必ず `unknown` を使用する。

## source_type の選択基準

| 値 | 意味 |
| --- | --- |
| `official` | プロバイダーの公式サイト・公式ドキュメントを根拠とする場合 |
| `benchmark` | ベンチマーク測定結果を根拠とする場合 |
| `manual` | 実際に操作・確認した結果を根拠とする場合 |
| `community` | コミュニティ情報（ブログ・フォーラム等）を根拠とする場合（推奨しない） |
| `unknown` | 情報源が不明な場合 |

公式情報と第三者情報・ベンチマーク情報を混同しない。

## verified_at の記載ルール

- 確認した日付を `YYYY-MM-DD` 形式で記載する。
- 確認日が不明な場合は `unknown` を使用する。
- 過去のデータを更新する場合は、確認した日付に更新する。

## verification_status の選択基準

| 値 | 意味 |
| --- | --- |
| `verified` | `source_url` のページで内容を確認済みの場合 |
| `unverified` | 情報源はあるが内容未確認の場合 |
| `unknown` | 検証状態が不明な場合（`source_type: unknown` のエントリ等） |

## 記載例

```yaml
# 公式サイトで確認済みの場合（数値）
- provider_id: example-vps
  feature_id: min_price_jpy
  value: 500
  source_type: official
  source_url: https://example.com/pricing/
  verified_at: "2024-01-01"
  verification_status: verified

# 公式サイトで確認済みの場合（boolean: 対応）
- provider_id: example-vps
  feature_id: ipv6_support
  value: true
  source_type: official
  source_url: https://example.com/specs/
  verified_at: "2024-01-01"
  verification_status: verified

# 公式サイトで非対応を確認済みの場合（boolean: 非対応）
- provider_id: example-vps
  feature_id: hourly_billing
  value: false
  source_type: official
  source_url: https://example.com/pricing/
  verified_at: "2024-01-01"
  verification_status: verified
  notes: 時間課金は非対応。月額のみ。

# 公式サイトで該当なしを確認済みの場合（string: 非対応・該当なし）
- provider_id: example-vps
  feature_id: price_2gb_hourly
  value: "-"
  source_type: official
  source_url: https://example.com/pricing/
  verified_at: "2024-01-01"
  verification_status: verified
  notes: 時間課金は非対応。月額のみ。

# 情報が未確認の場合
- provider_id: example-vps
  feature_id: bandwidth_gbps
  value: unknown
  source_type: unknown
  source_url: unknown
  verified_at: unknown
  verification_status: unknown
```

## 比較項目（features.yml）の管理方針

`features.yml` の各比較項目は、比較利用者にとって実際に有用かという観点を基準に管理します。

### 項目の維持・変更・削除の基準

| 方針 | 条件 |
| --- | --- |
| 維持 | 比較利用者にとって判断材料となる情報であり、将来的に確認できる可能性がある |
| 定義変更 | 項目自体は有用だが、対象範囲や定義が曖昧で誤解を招く可能性がある |
| 分割 | 1つの項目に複数の概念が混在しており、個別に確認できる |
| カテゴリ変更 | 別カテゴリの方が適切である |
| 詳細ページへ移動 | VPS比較表よりも個別プロバイダー詳細ページに記載すべき |
| 削除 | 定義が曖昧、他項目と重複、またはVPSの比較項目として不適切 |
| 調査対象外 | 将来的にも公式情報から確認困難であり、比較の優先度が低い |

### 削除しない条件

* 全プロバイダーで `unknown` であることだけを削除の理由にしない
* 公式情報から確認できないことを、「非対応」と判断しない
* 比較利用者にとって判断材料となり得る項目は維持する

### 認証・セキュリティ関連項目の扱い

`iso27001`・`isms`・`soc2`・`pci_dss` の各認証項目は、VPSサービス固有の認証ではなく、事業者全体または利用データセンターの認証取得状況を示す場合があります。証明書の適用範囲がVPSサービスに及ぶかどうかは、公式情報からは判断できないことがあるため、`notes` フィールドに補足情報を記載してください。

企業全体の認証情報とVPSサービスへの適用範囲を混同しないよう注意してください。

### データセンター設備関連項目の扱い

`power_redundancy`・`network_redundancy`・`seismic_resistance`・`dc_certification` などのデータセンター設備関連項目は、VPSサービス固有ではなく、利用データセンターの設備情報です。公式のデータセンター仕様ページや設備紹介ページから確認できる場合があります。

### 棚卸し履歴

#### 2026-07-23 棚卸し（Issue #96）

「公式情報で確認しづらい項目」の棚卸しを実施し、以下の方針を決定しました。

| 項目 | 旧ID | 方針 | 理由 |
| --- | --- | --- | --- |
| ISOアップロード | `iso_upload` | 削除 | `custom_iso`（カスタムISO）と概念が重複。カスタムISOの方が上位概念であり、URLマウント方式等を含む表現として適切 |
| OSテンプレート数 | `os_templates` | 削除 | カウント値は管理画面でしか確認できず公式情報から取得困難。頻繁に変動するため維持コストが高い。主要テンプレートは `standard_os_template` で記録可能 |
| DR（災害復旧）対応 | `dr_support` | 削除 | 定義が曖昧でVPSサービスのDR対応は明確な概念ではない。地理的冗長性は `cross_region_backup` 等で表現可能 |
| データセンター認証（SECURITY） | `datacenter_certification` | 削除 | `datacenter` カテゴリの `dc_certification` と重複。`dc_certification` を正とする |

以下の項目は定義を明確化しました（項目IDは変更なし）：

| 項目 | 変更内容 |
| --- | --- |
| `iso27001` | 事業者または利用データセンターの認証であり、VPSサービス固有の認証とは限らない旨を追記 |
| `isms` | 同上 |
| `soc2` | 同上 |
| `pci_dss` | 同上 |

以下の項目は全プロバイダーで `unknown` のまま残っていますが、比較価値があるため維持します：

* `bandwidth_gbps`（帯域目安）、`backup_retention_period`（バックアップ保持期間）、`backup_encryption`（バックアップ暗号化）、`cross_region_backup`（リージョン間バックアップ）、`backup_to_object_storage`（オブジェクトストレージへのバックアップ）
* `ansible_support`・`pulumi_support`・`webhook`・`metadata_service`・各SDK
* `iam_rbac`・`audit_log`・`iso27001`・`isms`・`soc2`・`pci_dss`
* `green_energy`・`zone_selection`・`network_redundancy`・`power_redundancy`・`seismic_resistance`・`same_region_redundancy`・`multi_region_deployment`・`dc_certification`
