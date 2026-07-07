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
