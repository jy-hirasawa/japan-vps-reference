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
| 高 | サポート / SLA | 62 / 65 | 95% |
| 高 | ディスク / NVMe / スナップショット / バックアップ | 37 / 55 | 67% |
| 高 | ネットワーク | 37 / 55 | 67% |
| 高 | バックアップ / イメージ保存 | 33 / 55 | 60% |
| 高 | 基本情報 | 25 / 30 | 83% |
| 高 | OS / テンプレート | 22 / 40 | 55% |
| 高 | 料金 | 2 / 45 | 4% |
| 高 | CPU / メモリ | 0 / 10 | 0% |
| 中 | セキュリティ | 70 / 70 | 100% |
| 中 | データセンター / リージョン | 60 / 60 | 100% |
| 中 | API / CLI / Terraform | 53 / 60 | 88% |

## プロバイダー別 unknown 集計

| Provider | 高 | 中 | 低 | 合計 |
| --- | --- | --- | --- | --- |
| Xserver VPS | 48 | 38 | 0 | 86 |
| WebARENA Indigo | 48 | 37 | 0 | 85 |
| KAGOYA CLOUD VPS | 41 | 38 | 0 | 79 |
| さくらのVPS | 41 | 35 | 0 | 76 |
| ConoHa VPS | 40 | 35 | 0 | 75 |

## 次に調査すべき項目（優先度: 高）

| カテゴリ | 項目 | unknown の Provider 数 | 公式URL付き根拠あり Provider 数 |
| --- | --- | --- | --- |
| ネットワーク | Floating IP | 4 / 5 | 1 / 5 |
| ネットワーク | IPv4 | 4 / 5 | 1 / 5 |
| ネットワーク | プライベートネットワーク | 4 / 5 | 1 / 5 |
| ネットワーク | ローカルネットワーク | 4 / 5 | 1 / 5 |
| ネットワーク | ロードバランサー | 4 / 5 | 1 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | イメージ保存 | 3 / 5 | 2 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | 自動スナップショット | 3 / 5 | 2 / 5 |
| ネットワーク | 転送量制限 | 3 / 5 | 2 / 5 |
| バックアップ / イメージ保存 | バックアップスケジュール設定 | 3 / 5 | 2 / 5 |
| 基本情報 | cloud-init明記 | 3 / 5 | 2 / 5 |
| OS / テンプレート | Docker系テンプレート | 2 / 5 | 3 / 5 |
| OS / テンプレート | アプリテンプレート | 2 / 5 | 3 / 5 |
| OS / テンプレート | カスタムISO | 2 / 5 | 3 / 5 |
| サポート / SLA | SLA稼働率（%） | 2 / 5 | 3 / 5 |
| ネットワーク | 逆引きDNS | 2 / 5 | 3 / 5 |
| バックアップ / イメージ保存 | バックアップ課金 | 2 / 5 | 3 / 5 |
| 基本情報 | スタートアップスクリプト | 2 / 5 | 3 / 5 |
| 料金 | 時間課金 | 2 / 5 | 3 / 5 |
| OS / テンプレート | KUSANAGIテンプレート | 1 / 5 | 4 / 5 |
| ディスク / NVMe / スナップショット / バックアップ | バックアップ機能 | 1 / 5 | 4 / 5 |
| ネットワーク | IPv6 | 1 / 5 | 4 / 5 |
| ネットワーク | 追加IPv4 | 1 / 5 | 4 / 5 |
| バックアップ / イメージ保存 | バックアップからの復元 | 1 / 5 | 4 / 5 |
| バックアップ / イメージ保存 | バックアップ世代数 | 1 / 5 | 4 / 5 |
| バックアップ / イメージ保存 | 自動バックアップ | 1 / 5 | 4 / 5 |

## 公式情報で確認しづらい項目

> 全プロバイダーで `unknown` かつ、`source_type: official` + `source_url` 付き根拠が未登録の項目です。

| 優先度 | カテゴリ | 項目 |
| --- | --- | --- |
| 高 | OS / テンプレート | AI系テンプレート |
| 高 | OS / テンプレート | ISOアップロード |
| 高 | OS / テンプレート | OSテンプレート数 |
| 高 | サポート / SLA | SLA文書URL |
| 高 | サポート / SLA | サポート窓口 |
| 高 | サポート / SLA | ステータスページ |
| 高 | サポート / SLA | チャットサポート |
| 高 | サポート / SLA | ナレッジベース / FAQ |
| 高 | サポート / SLA | メンテナンス情報ページ |
| 高 | サポート / SLA | メール通知 |
| 高 | サポート / SLA | 問い合わせフォーム |
| 高 | サポート / SLA | 日本語サポート |
| 高 | サポート / SLA | 法人向けサポート |
| 高 | サポート / SLA | 障害情報ページ |
| 高 | サポート / SLA | 電話サポート |
| 高 | ディスク / NVMe / スナップショット / バックアップ | NVMe明記 |
| 高 | ディスク / NVMe / スナップショット / バックアップ | SSD明記 |
| 高 | ディスク / NVMe / スナップショット / バックアップ | オブジェクトストレージ連携 |
| 高 | ディスク / NVMe / スナップショット / バックアップ | ストレージ種別 |
| 高 | ディスク / NVMe / スナップショット / バックアップ | ディスク拡張 |
| 高 | ディスク / NVMe / スナップショット / バックアップ | ディスク追加 |
| 高 | ネットワーク | VLAN |
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
| 中 | API / CLI / Terraform | CLI |
| 中 | API / CLI / Terraform | Pulumi対応 |
| 中 | API / CLI / Terraform | SDK（Go） |
| 中 | API / CLI / Terraform | SDK（Node.js） |
| 中 | API / CLI / Terraform | SDK（Python） |
| 中 | API / CLI / Terraform | Webhook |
| 中 | API / CLI / Terraform | メタデータサービス |
| 中 | セキュリティ | APIトークン |
| 中 | セキュリティ | DDoS保護 |
| 中 | セキュリティ | IAM / 権限管理 |
| 中 | セキュリティ | ISMS |
| 中 | セキュリティ | ISO27001 |
| 中 | セキュリティ | PCI DSS |
| 中 | セキュリティ | SOC 2 |
| 中 | セキュリティ | SSH鍵ログイン |
| 中 | セキュリティ | WAF |
| 中 | セキュリティ | セキュリティグループ |
| 中 | セキュリティ | データセンター認証 |
| 中 | セキュリティ | ファイアウォール機能 |
| 中 | セキュリティ | 二要素認証（管理画面） |
| 中 | セキュリティ | 監査ログ |
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
