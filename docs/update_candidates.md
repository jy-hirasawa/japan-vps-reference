# 未確認項目の更新候補一覧

> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。
> `unknown` のまま残っている項目を優先度付きで整理し、次に調査すべき項目を示します。
> `verified_at` が `180` 日以上前の項目は `STALE` と表示します。

## 優先度定義

- 高: バックアップ / イメージ保存, 基本情報, ネットワーク, OS / テンプレート, 料金, CPU / メモリ, ディスク / NVMe / スナップショット / バックアップ, サポート / SLA
- 中: OPS, セキュリティ, API / CLI / Terraform, データセンター / リージョン
- 低: 上記以外のカテゴリ

## カテゴリ別 unknown 集計

| 優先度 | カテゴリ | unknown / 総項目数 | unknown率 |
| --- | --- | --- | --- |
| 高 | OS / テンプレート | 21 / 40 | 52% |
| 高 | 基本情報 | 20 / 30 | 66% |
| 高 | ネットワーク | 4 / 55 | 7% |
| 高 | サポート / SLA | 2 / 65 | 3% |
| 高 | CPU / メモリ | 0 / 10 | 0% |
| 高 | ディスク / NVMe / スナップショット / バックアップ | 0 / 55 | 0% |
| 高 | バックアップ / イメージ保存 | 0 / 55 | 0% |
| 高 | 料金 | 0 / 45 | 0% |
| 中 | データセンター / リージョン | 60 / 60 | 100% |
| 中 | セキュリティ | 21 / 70 | 30% |
| 中 | API / CLI / Terraform | 0 / 60 | 0% |

## プロバイダー別 unknown 集計

| Provider | 高 | 中 | 低 | 合計 |
| --- | --- | --- | --- | --- |
| KAGOYA CLOUD VPS | 12 | 17 | 0 | 29 |
| WebARENA Indigo | 10 | 16 | 0 | 26 |
| Xserver VPS | 9 | 16 | 0 | 25 |
| ConoHa VPS | 8 | 18 | 0 | 26 |
| さくらのVPS | 8 | 14 | 0 | 22 |

## 次に調査すべき項目（優先度: 高）

| カテゴリ | 項目 | unknown の Provider 数 | 公式URL付き根拠あり Provider 数 |
| --- | --- | --- | --- |
| ネットワーク | 帯域目安（Gbps） | 4 / 5 | 1 / 5 |
| OS / テンプレート | Docker系テンプレート | 2 / 5 | 3 / 5 |
| OS / テンプレート | カスタムISO | 2 / 5 | 3 / 5 |
| OS / テンプレート | KUSANAGIテンプレート | 1 / 5 | 4 / 5 |
| OS / テンプレート | アプリテンプレート | 1 / 5 | 4 / 5 |
| サポート / SLA | SLA文書URL | 1 / 5 | 4 / 5 |
| サポート / SLA | SLA稼働率（%） | 1 / 5 | 4 / 5 |

## 公式情報で確認しづらい項目

> 全プロバイダーで `unknown` かつ、`source_type: official` + `source_url` 付き根拠が未登録の項目です。

| 優先度 | カテゴリ | 項目 |
| --- | --- | --- |
| 高 | OS / テンプレート | AI系テンプレート |
| 高 | OS / テンプレート | ISOアップロード |
| 高 | OS / テンプレート | OSテンプレート数 |
| 高 | 基本情報 | Linux対応 |
| 高 | 基本情報 | Windows公式対応 |
| 高 | 基本情報 | root権限 |
| 高 | 基本情報 | コンソール / VNC |
| 中 | セキュリティ | SSH鍵ログイン |
| 中 | セキュリティ | データセンター認証 |
| 中 | データセンター / リージョン | グリーン電力対応 |
| 中 | データセンター / リージョン | ゾーン選択 |
| 中 | データセンター / リージョン | データセンター所在地 |
| 中 | データセンター / リージョン | データセンター認証 |
| 中 | データセンター / リージョン | ネットワーク冗長 |
| 中 | データセンター / リージョン | リージョン選択 |
| 中 | データセンター / リージョン | 同一リージョン内冗長 |
| 中 | データセンター / リージョン | 国内リージョン数 |
| 中 | データセンター / リージョン | 海外リージョン |
| 中 | データセンター / リージョン | 耐震・免震 |
| 中 | データセンター / リージョン | 複数リージョン構成 |
| 中 | データセンター / リージョン | 電源冗長 |

## 公式URL更新候補

| Provider | Item | URL | verified_at | Status |
| --- | --- | --- | --- | --- |
| さくらのVPS | top | https://vps.sakura.ad.jp/ | unknown | UNKNOWN |
| さくらのVPS | pricing | https://vps.sakura.ad.jp/specification/ | unknown | UNKNOWN |
| さくらのVPS | specs | https://vps.sakura.ad.jp/specification/ | unknown | UNKNOWN |
| さくらのVPS | support | unknown | unknown | UNKNOWN |
| さくらのVPS | terms | https://vps.sakura.ad.jp/agreement/ | unknown | UNKNOWN |
| ConoHa VPS | top | https://www.conoha.jp/vps/ | unknown | UNKNOWN |
| ConoHa VPS | pricing | https://www.conoha.jp/vps/pricing/ | unknown | UNKNOWN |
| ConoHa VPS | specs | https://www.conoha.jp/vps/pricing/ | unknown | UNKNOWN |
| ConoHa VPS | support | unknown | unknown | UNKNOWN |
| ConoHa VPS | terms | https://www.conoha.jp/vps/agreement/ | unknown | UNKNOWN |
| Xserver VPS | top | https://vps.xserver.ne.jp/ | unknown | UNKNOWN |
| Xserver VPS | pricing | https://vps.xserver.ne.jp/price/ | unknown | UNKNOWN |
| Xserver VPS | specs | https://vps.xserver.ne.jp/price/ | unknown | UNKNOWN |
| Xserver VPS | support | unknown | unknown | UNKNOWN |
| Xserver VPS | terms | https://vps.xserver.ne.jp/agreement/ | unknown | UNKNOWN |
| WebARENA Indigo | top | https://web.arena.ne.jp/indigo/ | unknown | UNKNOWN |
| WebARENA Indigo | pricing | https://web.arena.ne.jp/indigo/price/ | unknown | UNKNOWN |
| WebARENA Indigo | specs | https://web.arena.ne.jp/indigo/price/ | unknown | UNKNOWN |
| WebARENA Indigo | support | unknown | unknown | UNKNOWN |
| WebARENA Indigo | terms | unknown | unknown | UNKNOWN |
| KAGOYA CLOUD VPS | top | https://www.kagoya.jp/cloud/vps/ | unknown | UNKNOWN |
| KAGOYA CLOUD VPS | pricing | https://www.kagoya.jp/vps/function-plan/ | unknown | UNKNOWN |
| KAGOYA CLOUD VPS | specs | https://www.kagoya.jp/vps/function-plan/ | unknown | UNKNOWN |
| KAGOYA CLOUD VPS | support | unknown | unknown | UNKNOWN |
| KAGOYA CLOUD VPS | terms | unknown | unknown | UNKNOWN |
