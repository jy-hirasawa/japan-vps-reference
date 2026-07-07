# VPS 比較テーブル

> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。
> 「不明」は公式情報が確認できないことを示します。
> 値の横の `🔗` は情報源リンク、`(YYYY-MM-DD)` は確認日です。

## 最終確認日

| Provider | 最終確認日 |
| --- | --- |
| さくらのVPS | 2026-07-07 |
| ConoHa VPS | 2026-07-07 |
| Xserver VPS | 2026-07-07 |
| WebARENA Indigo | 2026-07-07 |
| KAGOYA CLOUD VPS | 2026-07-07 |

## 公式URL

### さくらのVPS

| 項目 | URL |
| --- | --- |
| 公式サイト | [https://vps.sakura.ad.jp/](https://vps.sakura.ad.jp/) |
| 料金ページ | [https://vps.sakura.ad.jp/specification/](https://vps.sakura.ad.jp/specification/) |
| 仕様ページ | [https://vps.sakura.ad.jp/specification/](https://vps.sakura.ad.jp/specification/) |
| 利用規約 | [https://vps.sakura.ad.jp/agreement/](https://vps.sakura.ad.jp/agreement/) |
| 最終確認日 | 未確認 |

### ConoHa VPS

| 項目 | URL |
| --- | --- |
| 公式サイト | [https://www.conoha.jp/vps/](https://www.conoha.jp/vps/) |
| 料金ページ | [https://www.conoha.jp/vps/pricing/](https://www.conoha.jp/vps/pricing/) |
| 仕様ページ | [https://www.conoha.jp/vps/pricing/](https://www.conoha.jp/vps/pricing/) |
| 利用規約 | [https://www.conoha.jp/vps/agreement/](https://www.conoha.jp/vps/agreement/) |
| 最終確認日 | 未確認 |

### Xserver VPS

| 項目 | URL |
| --- | --- |
| 公式サイト | [https://vps.xserver.ne.jp/](https://vps.xserver.ne.jp/) |
| 料金ページ | [https://vps.xserver.ne.jp/price/](https://vps.xserver.ne.jp/price/) |
| 仕様ページ | [https://vps.xserver.ne.jp/price/](https://vps.xserver.ne.jp/price/) |
| 利用規約 | [https://vps.xserver.ne.jp/agreement/](https://vps.xserver.ne.jp/agreement/) |
| 最終確認日 | 未確認 |

### WebARENA Indigo

| 項目 | URL |
| --- | --- |
| 公式サイト | [https://web.arena.ne.jp/indigo/](https://web.arena.ne.jp/indigo/) |
| 料金ページ | [https://web.arena.ne.jp/indigo/price/](https://web.arena.ne.jp/indigo/price/) |
| 仕様ページ | [https://web.arena.ne.jp/indigo/price/](https://web.arena.ne.jp/indigo/price/) |
| 最終確認日 | 未確認 |

### KAGOYA CLOUD VPS

| 項目 | URL |
| --- | --- |
| 公式サイト | [https://www.kagoya.jp/cloud/vps/](https://www.kagoya.jp/cloud/vps/) |
| 料金ページ | [https://www.kagoya.jp/vps/function-plan/](https://www.kagoya.jp/vps/function-plan/) |
| 仕様ページ | [https://www.kagoya.jp/vps/function-plan/](https://www.kagoya.jp/vps/function-plan/) |
| 最終確認日 | 未確認 |


## 基本情報

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | root権限 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 2 | Linux対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 3 | Windows公式対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 4 | コンソール / VNC | 不明 | 不明 | 不明 | 不明 | 不明 |
| 5 | スタートアップスクリプト | ✅ [🔗](https://manual.sakura.ad.jp/vps/startupscript/startupscript.html) (2026-07-07) | ✅ [🔗](https://vps.conoha.jp/function/startupscript/) (2026-07-07) | 不明 | 不明 | ✅ [🔗](https://www.kagoya.jp/cloud/vps/manual/instance/) (2026-07-07) |
| 6 | cloud-init明記 | 不明 | 不明 | 不明 | ✅ [🔗](https://web.arena.ne.jp/indigo/spec/) (2026-07-07) | ✅ [🔗](https://www.kagoya.jp/cloud/vps/manual/instance/) (2026-07-07) |

## OS / テンプレート

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 標準OSテンプレート | AlmaLinux, Rocky Linux, Ubuntu, Debian, FreeBSD [🔗](https://vps.sakura.ad.jp/specification/#specification_os) (2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu, Debian, Fedora, FreeBSD, Windows Server [🔗](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template) (2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu, Debian, Fedora [🔗](https://vps.xserver.ne.jp/os-list.php) (2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu, Debian, Windows Server [🔗](https://web.arena.ne.jp/indigo/spec/os.html) (2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu [🔗](https://www.kagoya.jp/cloud/vps/manual/list/) (2026-07-07) |
| 2 | OSテンプレート数 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 3 | アプリテンプレート | ✅ [🔗](https://vps.sakura.ad.jp/specification/#specification_application) (2026-07-07) | ✅ [🔗](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template) (2026-07-07) | ✅ [🔗](https://vps.xserver.ne.jp/os-list.php) (2026-07-07) | 不明 | 不明 |
| 4 | KUSANAGIテンプレート | ✅ [🔗](https://vps.sakura.ad.jp/specification/#specification_application) (2026-07-07) | ✅ [🔗](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template) (2026-07-07) | ✅ [🔗](https://vps.xserver.ne.jp/support/manual/man_server_app_use_kusanagi.php) (2026-07-07) | ✅ [🔗](https://web.arena.ne.jp/indigo/spec/kusanagi.html) (2026-07-07) | 不明 |
| 5 | Docker系テンプレート | ✅ [🔗](https://vps.sakura.ad.jp/specification/#specification_application) (2026-07-07) | ✅ [🔗](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template) (2026-07-07) | ✅ [🔗](https://vps.xserver.ne.jp/os-list.php) (2026-07-07) | 不明 | 不明 |
| 6 | AI系テンプレート | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | カスタムISO | ✅ [🔗](https://manual.sakura.ad.jp/vps/os-reinstall/iso-install.html) (2026-07-07) | ✅ [🔗](https://support.conoha.jp/vps/iso-upload/) (2026-07-07) | 不明 | 不明 | ✅ [🔗](https://www.kagoya.jp/support/category/cloud/vps/vps_manual/iso/) (2026-07-07) |
| 8 | ISOアップロード | 不明 | 不明 | 不明 | 不明 | 不明 |

## 料金

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 最低月額料金（円） | 643 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 460 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1496 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 319 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 550 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 2 | 時間課金 | ❌ [🔗](https://vps.sakura.ad.jp/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/pricing/) (2024-01-01) | ❌ [🔗](https://vps.xserver.ne.jp/price/) (2024-01-01) | 不明 | 不明 |
| 3 | 2GBプラン月額（円・税込） | 1738 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 1259 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1496 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 814 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 770 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 4 | 2GBプラン時間課金（円/時・税込） | - [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 3.7 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 1.27 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | - [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 5 | 4GBプラン月額（円・税込） | 3520 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 2189 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 1630 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 1760 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 6 | 4GBプラン時間課金（円/時・税込） | - [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 6.6 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 2.55 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | - [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 7 | 月額上限（円・税込） | - [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 751 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 319 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 550 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 8 | 初期費用（円・税込） | 0 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 0 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 0 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 0 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 0 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 9 | 最低利用期間 | 1ヶ月 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | なし [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1ヶ月 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | なし [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | なし [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |

## CPU / メモリ

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 最小vCPU数 | 1 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 1 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 3 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 1 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 1 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 2 | 最小RAM（GB） | 0.5 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 0.5 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 2 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 0.75 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 1 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |

## ディスク / NVMe / スナップショット / バックアップ

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ディスク容量（GB） | 25 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 30 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 50 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 20 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 100 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 2 | ストレージ種別 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 3 | NVMe明記 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 4 | SSD明記 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 5 | ディスク追加 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 6 | ディスク拡張 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | スナップショット | ✅ [🔗](https://vps.sakura.ad.jp/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/function/) (2024-01-01) | ✅ [🔗](https://vps.xserver.ne.jp/support/manual/man_server_image.php) (2026-07-07) | ✅ [🔗](https://web.arena.ne.jp/indigo/spec/) (2026-07-07) | ✅ [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 8 | 自動スナップショット | 不明 | ❌ [🔗](https://support.conoha.jp/v/snapshot/) (2026-07-07) | 不明 | 不明 | ✅ [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 9 | バックアップ機能 | ✅ [🔗](https://vps.sakura.ad.jp/feature/backup/) (2026-07-07) | ✅ [🔗](https://support.conoha.jp/v/vps-autobackup/) (2026-07-07) | ✅ [🔗](https://vps.xserver.ne.jp/support/faq/service_server_backup.php) (2026-07-07) | 不明 | ✅ [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 10 | イメージ保存 | 不明 | 不明 | ✅ [🔗](https://vps.xserver.ne.jp/support/manual/man_server_image.php) (2026-07-07) | 不明 | ✅ [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 11 | オブジェクトストレージ連携 | 不明 | 不明 | 不明 | 不明 | 不明 |

## ネットワーク

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | IPv4 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 2 | IPv6 | ✅ [🔗](https://vps.sakura.ad.jp/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/) (2024-01-01) | 不明 | 不明 | 不明 |
| 3 | 追加IPv4 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 4 | 逆引きDNS | 不明 | 不明 | 不明 | 不明 | 不明 |
| 5 | 転送量制限 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 6 | 帯域目安（Gbps） | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | ローカルネットワーク | 不明 | 不明 | 不明 | 不明 | 不明 |
| 8 | プライベートネットワーク | 不明 | 不明 | 不明 | 不明 | 不明 |
| 9 | VLAN | 不明 | 不明 | 不明 | 不明 | 不明 |
| 10 | ロードバランサー | 不明 | 不明 | 不明 | 不明 | 不明 |
| 11 | Floating IP | 不明 | 不明 | 不明 | 不明 | 不明 |

## セキュリティ

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SSH鍵ログイン | 不明 | 不明 | 不明 | 不明 | 不明 |
| 2 | ファイアウォール機能 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 3 | DDoS保護 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 4 | WAF | 不明 | 不明 | 不明 | 不明 | 不明 |
| 5 | セキュリティグループ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 6 | 二要素認証（管理画面） | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | APIトークン | 不明 | 不明 | 不明 | 不明 | 不明 |
| 8 | IAM / 権限管理 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 9 | 監査ログ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 10 | ISO27001 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 11 | ISMS | 不明 | 不明 | 不明 | 不明 | 不明 |
| 12 | SOC 2 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 13 | PCI DSS | 不明 | 不明 | 不明 | 不明 | 不明 |
| 14 | データセンター認証 | 不明 | 不明 | 不明 | 不明 | 不明 |

## バックアップ / イメージ保存

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 手動バックアップ | ✅ [🔗](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/) (2026-07-07) | ✅ [🔗](https://support.conoha.jp/v/snapshot/) (2026-07-07) | ✅ [🔗](https://vps.xserver.ne.jp/support/manual/man_server_image.php) (2026-07-07) | ✅ [🔗](https://web.arena.ne.jp/indigo/spec/) (2026-07-07) | ✅ [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 2 | 自動バックアップ | ✅ [🔗](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/) (2026-07-07) | ✅ [🔗](https://support.conoha.jp/v/vps-autobackup/) (2026-07-07) | ✅ [🔗](https://vps.xserver.ne.jp/support/faq/service_server_backup.php) (2026-07-07) | 不明 | ✅ [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 3 | バックアップスケジュール設定 | ✅ [🔗](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/) (2026-07-07) | ❌ [🔗](https://doc.conoha.jp/products/vps-v3/storage-v3/autobackup-v3/) (2026-07-07) | 不明 | 不明 | 不明 |
| 4 | バックアップ保持期間 | 不明 | 最大30世代（VPS 3.0）、最大3世代（VPS 2.0） [🔗](https://doc.conoha.jp/products/vps-v3/storage-v3/autobackup-v3/) (2026-07-07) | 不明 | 不明 | 不明 |
| 5 | バックアップ世代数 | 不明 | 14世代（デフォルト）、最大30世代（VPS 3.0） [🔗](https://doc.conoha.jp/products/vps-v3/storage-v3/autobackup-v3/) (2026-07-07) | ビジネスプラン標準1世代、バックアップ拡張オプションで最大3世代 [🔗](https://vps.xserver.ne.jp/support/faq/service_server_backup.php) (2026-07-07) | 最大5個/インスタンス（スナップショット） [🔗](https://web.arena.ne.jp/indigo/spec/) (2026-07-07) | 最大7世代（定期スナップショット） [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 6 | バックアップからの復元 | ✅ [🔗](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/) (2026-07-07) | ✅ [🔗](https://support.conoha.jp/v/vps-autobackup/) (2026-07-07) | 不明 | ✅ [🔗](https://web.arena.ne.jp/indigo/spec/) (2026-07-07) | ✅ [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |
| 7 | バックアップ暗号化 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 8 | オブジェクトストレージへのバックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 9 | リージョン間バックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 10 | DR（災害復旧）対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 11 | バックアップ課金 | 有料オプション（Acronis Cyber Protect Cloud: 1,760円/月〜(100GB)） [🔗](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/) (2026-07-07) | 有料オプション（世代数により料金変動） [🔗](https://support.conoha.jp/v/vps-autobackup/) (2026-07-07) | 不明 | 不明 | 有料（容量課金：スナップショット10GBあたり日額4.4円） [🔗](https://www.kagoya.jp/vps/feature/customize/) (2026-07-07) |

## API / CLI / Terraform

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | REST API | ✅ [🔗](https://manual.sakura.ad.jp/vps/api/) (2026-07-07) | ✅ [🔗](https://www.conoha.jp/vps/function/api/) (2026-07-07) | 不明 | ✅ [🔗](https://web.arena.ne.jp/indigo/spec/) (2026-07-07) | 不明 |
| 2 | OpenAPI公開 | ✅ [🔗](https://manual.sakura.ad.jp/vps/api/api-doc/index.html) (2026-07-07) | ✅ [🔗](https://github.com/gmo-internet/conoha_vps_openapi) (2026-07-07) | 不明 | 不明 | 不明 |
| 3 | CLI | 不明 | 不明 | 不明 | 不明 | 不明 |
| 4 | Terraform Provider | 不明 | ✅ [🔗](https://vps.conoha.jp/terraform_provider/) (2026-07-07) | 不明 | 不明 | 不明 |
| 5 | Pulumi対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 6 | Ansible対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | メタデータサービス | 不明 | 不明 | 不明 | 不明 | 不明 |
| 8 | APIレート制限公開 | ✅ [🔗](https://manual.sakura.ad.jp/vps/api/api-doc/index.html) (2026-07-07) | 不明 | 不明 | 不明 | 不明 |
| 9 | Webhook | 不明 | 不明 | 不明 | 不明 | 不明 |
| 10 | SDK（Go） | 不明 | 不明 | 不明 | 不明 | 不明 |
| 11 | SDK（Python） | 不明 | 不明 | 不明 | 不明 | 不明 |
| 12 | SDK（Node.js） | 不明 | 不明 | 不明 | 不明 | 不明 |

## サポート / SLA

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SLA稼働率（%） | 99.99 [🔗](https://vps.sakura.ad.jp/agreement/) (2024-01-01) | 99.99 [🔗](https://www.conoha.jp/vps/agreement/) (2024-01-01) | 99.99 [🔗](https://vps.xserver.ne.jp/agreement/) (2024-01-01) | 不明 | 不明 |
| 2 | SLA文書URL | 不明 | 不明 | 不明 | 不明 | 不明 |
| 3 | ステータスページ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 4 | 障害情報ページ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 5 | メンテナンス情報ページ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 6 | メール通知 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | サポート窓口 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 8 | 電話サポート | 不明 | 不明 | 不明 | 不明 | 不明 |
| 9 | チャットサポート | 不明 | 不明 | 不明 | 不明 | 不明 |
| 10 | 問い合わせフォーム | 不明 | 不明 | 不明 | 不明 | 不明 |
| 11 | 法人向けサポート | 不明 | 不明 | 不明 | 不明 | 不明 |
| 12 | 日本語サポート | 不明 | 不明 | 不明 | 不明 | 不明 |
| 13 | ナレッジベース / FAQ | 不明 | 不明 | 不明 | 不明 | 不明 |

## データセンター / リージョン

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 国内リージョン数 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 2 | 海外リージョン | 不明 | 不明 | 不明 | 不明 | 不明 |
| 3 | データセンター所在地 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 4 | リージョン選択 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 5 | ゾーン選択 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 6 | 同一リージョン内冗長 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | 複数リージョン構成 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 8 | 電源冗長 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 9 | ネットワーク冗長 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 10 | 耐震・免震 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 11 | データセンター認証 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 12 | グリーン電力対応 | 不明 | 不明 | 不明 | 不明 | 不明 |

## 凡例

| 表示 | 意味 |
| --- | --- |
| ✅ | 対応あり（確認済み） |
| ❌ | 非対応（確認済み） |
| `-` | プランなし・該当なし（確認済み） |
| 不明 | 公式情報が確認できていない |

> 値の表現ルールの詳細は [docs/data-policy.md](data-policy.md) を参照してください。
