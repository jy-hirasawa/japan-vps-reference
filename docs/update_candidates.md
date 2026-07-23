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
| 高 | バックアップ / イメージ保存 | 28 / 55 | 50% |
| 高 | 基本情報 | 24 / 30 | 80% |
| 高 | OS / テンプレート | 21 / 40 | 52% |
| 高 | ネットワーク | 21 / 55 | 38% |
| 高 | ディスク / NVMe / スナップショット / バックアップ | 13 / 55 | 23% |
| 高 | サポート / SLA | 8 / 65 | 12% |
| 高 | 料金 | 2 / 45 | 4% |
| 高 | CPU / メモリ | 0 / 10 | 0% |
| 中 | API / CLI / Terraform | 52 / 60 | 86% |
| 中 | セキュリティ | 52 / 70 | 74% |
| 中 | データセンター / リージョン | 50 / 60 | 83% |

## プロバイダー別 unknown 集計

| Provider | 高 | 中 | 低 | 合計 |
| --- | --- | --- | --- | --- |
| WebARENA Indigo | 32 | 32 | 0 | 64 |
| Xserver VPS | 26 | 34 | 0 | 60 |
| KAGOYA CLOUD VPS | 21 | 35 | 0 | 56 |
| さくらのVPS | 21 | 28 | 0 | 49 |
| ConoHa VPS | 17 | 25 | 0 | 42 |

## 次に調査すべき項目（優先度: 高）

| カテゴリ | 項目 | unknown の Provider 数 | 公式URL付き根拠あり Provider 数 |
| --- | --- | --- | --- |
| ディスク / NVMe / スナップショット / バックアップ | オブジェクトストレージ連携 | 4 / 5 | 1 / 5 |
| ネットワーク | Floating IP | 4 / 5 | 1 / 5 |
| ネットワーク | ロードバランサー | 4 / 5 | 1 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | ディスク追加 | 3 / 5 | 2 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | 自動スナップショット | 3 / 5 | 2 / 5 |
| ネットワーク | VLAN | 3 / 5 | 2 / 5 |
| OS / テンプレート | Docker系テンプレート | 2 / 5 | 3 / 5 |
| OS / テンプレート | カスタムISO | 2 / 5 | 3 / 5 |
| サポート / SLA | SLA文書URL | 2 / 5 | 3 / 5 |
| サポート / SLA | 法人向けサポート | 2 / 5 | 3 / 5 |
| サポート / SLA | 電話サポート | 2 / 5 | 3 / 5 |
| ネットワーク | プライベートネットワーク | 2 / 5 | 3 / 5 |
| ネットワーク | ローカルネットワーク | 2 / 5 | 3 / 5 |
| バックアップ / イメージ保存 | バックアップスケジュール設定 | 2 / 5 | 3 / 5 |
| 基本情報 | cloud-init明記 | 2 / 5 | 3 / 5 |
| 基本情報 | スタートアップスクリプト | 2 / 5 | 3 / 5 |
| 料金 | 時間課金 | 2 / 5 | 3 / 5 |
| OS / テンプレート | KUSANAGIテンプレート | 1 / 5 | 4 / 5 |
| OS / テンプレート | アプリテンプレート | 1 / 5 | 4 / 5 |
| サポート / SLA | SLA稼働率（%） | 1 / 5 | 4 / 5 |
| サポート / SLA | チャットサポート | 1 / 5 | 4 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | NVMe明記 | 1 / 5 | 4 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | イメージ保存 | 1 / 5 | 4 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | ディスク拡張 | 1 / 5 | 4 / 5 |
| ネットワーク | 追加IPv4 | 1 / 5 | 4 / 5 |
| バックアップ / イメージ保存 | バックアップ世代数 | 1 / 5 | 4 / 5 |

## 公式情報で確認しづらい項目

> 全プロバイダーで `unknown` かつ、`source_type: official` + `source_url` 付き根拠が未登録の項目です。

| 優先度 | カテゴリ | 項目 |
| --- | --- | --- |
| 高 | OS / テンプレート | AI系テンプレート |
| 高 | OS / テンプレート | ISOアップロード |
| 高 | OS / テンプレート | OSテンプレート数 |
| 高 | ネットワーク | 帯域目安（Gbps） |
| 高 | バックアップ / イメージ保存 | DR（災害復旧）対応 |
| 高 | バックアップ / イメージ保存 | オブジェクトストレージへのバックアップ |
| 高 | バックアップ / イメージ保存 | バックアップ保持期間 |
| 高 | バックアップ / イメージ保存 | バックアップ暗号化 |
| 高 | バックアップ / イメージ保存 | リージョン間バックアップ |
| 高 | 基本情報 | Linux対応 |
| 高 | 基本情報 | Windows公式対応 |
| 高 | 基本情報 | root権限 |
| 高 | 基本情報 | コンソール / VNC |
| 中 | API / CLI / Terraform | Ansible対応 |
| 中 | API / CLI / Terraform | Pulumi対応 |
| 中 | API / CLI / Terraform | SDK（Go） |
| 中 | API / CLI / Terraform | SDK（Node.js） |
| 中 | API / CLI / Terraform | SDK（Python） |
| 中 | API / CLI / Terraform | Webhook |
| 中 | API / CLI / Terraform | メタデータサービス |
| 中 | セキュリティ | IAM / 権限管理 |
| 中 | セキュリティ | ISMS |
| 中 | セキュリティ | ISO27001 |
| 中 | セキュリティ | PCI DSS |
| 中 | セキュリティ | SOC 2 |
| 中 | セキュリティ | SSH鍵ログイン |
| 中 | セキュリティ | データセンター認証 |
| 中 | セキュリティ | 監査ログ |
| 中 | データセンター / リージョン | グリーン電力対応 |
| 中 | データセンター / リージョン | ゾーン選択 |
| 中 | データセンター / リージョン | データセンター認証 |
| 中 | データセンター / リージョン | ネットワーク冗長 |
| 中 | データセンター / リージョン | 同一リージョン内冗長 |
| 中 | データセンター / リージョン | 耐震・免震 |
| 中 | データセンター / リージョン | 複数リージョン構成 |
| 中 | データセンター / リージョン | 電源冗長 |

## 公式URL更新候補

| Provider | Item | URL | verified_at | Status |
| --- | --- | --- | --- | --- |
| さくらのVPS | top | https://vps.sakura.ad.jp/ | 2026-07-22 | VERIFIED |
| さくらのVPS | pricing | https://vps.sakura.ad.jp/specification/ | 2026-07-22 | VERIFIED |
| さくらのVPS | specs | https://vps.sakura.ad.jp/specification/ | 2026-07-22 | VERIFIED |
| さくらのVPS | support | https://manual.sakura.ad.jp/vps/ | 2026-07-22 | VERIFIED |
| さくらのVPS | terms | https://vps.sakura.ad.jp/agreement/ | 2026-07-22 | VERIFIED |
| ConoHa VPS | top | https://www.conoha.jp/vps/ | 2026-07-22 | VERIFIED |
| ConoHa VPS | pricing | https://www.conoha.jp/vps/pricing/ | 2026-07-22 | VERIFIED |
| ConoHa VPS | specs | https://www.conoha.jp/vps/pricing/ | 2026-07-22 | VERIFIED |
| ConoHa VPS | support | https://support.conoha.jp/vps/ | 2026-07-22 | VERIFIED |
| ConoHa VPS | terms | https://www.conoha.jp/vps/agreement/ | 2026-07-22 | VERIFIED |
| Xserver VPS | top | https://vps.xserver.ne.jp/ | 2026-07-22 | VERIFIED |
| Xserver VPS | pricing | https://vps.xserver.ne.jp/price/ | 2026-07-22 | VERIFIED |
| Xserver VPS | specs | https://vps.xserver.ne.jp/price/ | 2026-07-22 | VERIFIED |
| Xserver VPS | support | https://vps.xserver.ne.jp/support/ | 2026-07-22 | VERIFIED |
| Xserver VPS | terms | https://vps.xserver.ne.jp/agreement/ | 2026-07-22 | VERIFIED |
| WebARENA Indigo | top | https://web.arena.ne.jp/indigo/ | 2026-07-22 | VERIFIED |
| WebARENA Indigo | pricing | https://web.arena.ne.jp/indigo/price/ | 2026-07-22 | VERIFIED |
| WebARENA Indigo | specs | https://web.arena.ne.jp/indigo/price/ | 2026-07-22 | VERIFIED |
| WebARENA Indigo | support | https://web.arena.ne.jp/indigo/support/ | 2026-07-22 | VERIFIED |
| WebARENA Indigo | terms | https://web.arena.ne.jp/rule/ | 2026-07-22 | VERIFIED |
| KAGOYA CLOUD VPS | top | https://www.kagoya.jp/cloud/vps/ | 2026-07-22 | VERIFIED |
| KAGOYA CLOUD VPS | pricing | https://www.kagoya.jp/vps/function-plan/ | 2026-07-22 | VERIFIED |
| KAGOYA CLOUD VPS | specs | https://www.kagoya.jp/vps/function-plan/ | 2026-07-22 | VERIFIED |
| KAGOYA CLOUD VPS | support | https://support.kagoya.jp/vps/ | 2026-07-22 | VERIFIED |
| KAGOYA CLOUD VPS | terms | https://www.kagoya.jp/terms/vps/ | 2026-07-22 | VERIFIED |
