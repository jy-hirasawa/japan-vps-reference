# VPS 比較テーブル

> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。
> 「不明」は公式情報が確認できないことを示します。
> 値の横の `[公式]` は情報源リンク、`(YYYY-MM-DD)` は確認日です。

## 最終確認日

| Provider | 最終確認日 |
| --- | --- |
| さくらのVPS | 2026-07-08 |
| ConoHa VPS | 2026-07-08 |
| Xserver VPS | 2026-07-08 |
| WebARENA Indigo | 2026-07-08 |
| KAGOYA CLOUD VPS | 2026-07-08 |

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
| 5 | スタートアップスクリプト | ✅ [公式](https://manual.sakura.ad.jp/vps/startupscript/startupscript.html)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/startupscript/)<br>(2026-07-07) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/cloud/vps/manual/instance/)<br>(2026-07-07) |
| 6 | cloud-init明記 | ❌ [公式](https://manual.sakura.ad.jp/vps/startupscript/startupscript.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/v/startupscript/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/cloud/vps/manual/instance/)<br>(2026-07-07) |

## OS / テンプレート

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 標準OSテンプレート | AlmaLinux, Rocky Linux, Ubuntu, Debian, FreeBSD [公式](https://vps.sakura.ad.jp/specification/#specification_os)<br>(2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu, Debian, Fedora, FreeBSD, Windows Server [公式](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template)<br>(2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu, Debian, Fedora [公式](https://vps.xserver.ne.jp/os-list.php)<br>(2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu, Debian, Windows Server [公式](https://web.arena.ne.jp/indigo/spec/os.html)<br>(2026-07-07) | AlmaLinux, Rocky Linux, Ubuntu [公式](https://www.kagoya.jp/cloud/vps/manual/list/)<br>(2026-07-07) |
| 2 | OSテンプレート数 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 3 | アプリテンプレート | ✅ [公式](https://vps.sakura.ad.jp/specification/#specification_application)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/os-list.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/kusanagi.html)<br>(2026-07-08) | 不明 |
| 4 | KUSANAGIテンプレート | ✅ [公式](https://vps.sakura.ad.jp/specification/#specification_application)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_app_use_kusanagi.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/kusanagi.html)<br>(2026-07-07) | 不明 |
| 5 | Docker系テンプレート | ✅ [公式](https://vps.sakura.ad.jp/specification/#specification_application)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/os-list.php)<br>(2026-07-07) | 不明 | 不明 |
| 6 | AI系テンプレート | 不明 | 不明 | 不明 | 不明 | 不明 |
| 7 | カスタムISO | ✅ [公式](https://manual.sakura.ad.jp/vps/os-reinstall/iso-install.html)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/vps/iso-upload/)<br>(2026-07-07) | 不明 | 不明 | ✅ [公式](https://www.kagoya.jp/support/category/cloud/vps/vps_manual/iso/)<br>(2026-07-07) |
| 8 | ISOアップロード | 不明 | 不明 | 不明 | 不明 | 不明 |

## 料金

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 最低月額料金（円） | 643 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 460 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1496 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 319 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 550 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 2 | 時間課金 | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2024-01-01) | ✅ [公式](https://www.conoha.jp/vps/pricing/)<br>(2024-01-01) | ❌ [公式](https://vps.xserver.ne.jp/price/)<br>(2024-01-01) | ❌ [公式](https://web.arena.ne.jp/indigo/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 3 | 2GBプラン月額（円・税込） | 1738 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 1259 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1496 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 814 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 770 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 4 | 2GBプラン時間課金（円/時・税込） | - [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 3.7 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 1.27 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | - [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 5 | 4GBプラン月額（円・税込） | 3520 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 2189 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 1630 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 1760 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 6 | 4GBプラン時間課金（円/時・税込） | - [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 6.6 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 2.55 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | - [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 7 | 月額上限（円・税込） | - [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 751 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 319 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 550 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 8 | 初期費用（円・税込） | 0 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 0 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 0 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 0 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 0 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 9 | 最低利用期間 | 1ヶ月 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | なし [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1ヶ月 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | なし [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | なし [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |

## CPU / メモリ

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 最小vCPU数 | 1 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 1 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 3 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 1 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 1 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 2 | 最小RAM（GB） | 0.5 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 0.5 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 2 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 0.75 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 1 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |

## ディスク / NVMe / スナップショット / バックアップ

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ディスク容量（GB） | 25 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 30 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 50 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 20 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 100 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 2 | ストレージ種別 | SSD（NVMe対応） [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-08) | NVMe SSD（分散ストレージ） [公式](https://doc.conoha.jp/products/vps-v3/storage-v3/boot-storage-v3/)<br>(2026-07-08) | NVMe SSD [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | SSD [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | NVMe SSD [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 3 | NVMe明記 | ✅ [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-08) | ✅ [公式](https://doc.conoha.jp/products/vps-v3/storage-v3/boot-storage-v3/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/)<br>(2026-07-08) |
| 4 | SSD明記 | ✅ [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-08) | ✅ [公式](https://doc.conoha.jp/products/vps-v3/storage-v3/boot-storage-v3/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 5 | ディスク追加 | ✅ [公式](https://vps.sakura.ad.jp/feature/nfs.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/v/addssd/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/support/manual/man_server_storage_expansion.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://support.kagoya.jp/vps/faq/index.php?action=artikel&cat=1&id=5)<br>(2026-07-08) |
| 6 | ディスク拡張 | ✅ [公式](https://manual.sakura.ad.jp/vps/server/storage-change-option.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/v/changedisk/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_storage_expansion.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/vps/charge/index.html)<br>(2026-07-08) |
| 7 | スナップショット | ✅ [公式](https://vps.sakura.ad.jp/)<br>(2024-01-01) | ✅ [公式](https://www.conoha.jp/vps/function/)<br>(2024-01-01) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_image.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 8 | 自動スナップショット | ❌ [公式](https://vps.sakura.ad.jp/faq/)<br>(2026-07-08) | ❌ [公式](https://support.conoha.jp/v/snapshot/)<br>(2026-07-07) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 9 | バックアップ機能 | ✅ [公式](https://vps.sakura.ad.jp/feature/backup/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 10 | イメージ保存 | ❌ [公式](https://vps.sakura.ad.jp/faq/)<br>(2026-07-08) | ✅ [公式](https://vps.conoha.jp/function/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_image.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 11 | オブジェクトストレージ連携 | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/vps/guide/objectstorage/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |

## ネットワーク

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | IPv4 | 静的グローバルIPv4 1個標準付与 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-08) | 静的グローバルIPv4 1個標準付与 [公式](https://vps.conoha.jp/spec/)<br>(2026-07-08) | 静的グローバルIPv4 1個標準付与 [公式](https://vps.xserver.ne.jp/spec.php)<br>(2026-07-08) | 768MBプランはなし（IPv6のみ）/ 1GB以上は1個 [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | 静的グローバルIPv4 1個標準付与 [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 2 | IPv6 | ✅ [公式](https://manual.sakura.ad.jp/vps/network/index.html)<br>(2026-07-07) | ✅ [公式](https://doc.conoha.jp/products/vps-v3/network-v3/ipv6-v3/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/news_detail.php?view_id=11190)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://support.kagoya.jp/vps/charge/index.html)<br>(2026-07-07) |
| 3 | 追加IPv4 | ❌ [公式](https://manual.sakura.ad.jp/vps/support/technical/ip-address.html)<br>(2026-07-07) | ✅ [公式](https://doc.conoha.jp/products/vps-v2/network-v2/addip-v2/)<br>(2026-07-07) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://support.kagoya.jp/vps/manual/index.php?action=artikel&cat=18&id=69)<br>(2026-07-07) |
| 4 | 逆引きDNS | ✅ [公式](https://manual.sakura.ad.jp/vps/support/technical/ip-address.html)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/vps/faq/ip-q/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://support.kagoya.jp/vps/manual/index.php?action=artikel&cat=40&id=51)<br>(2026-07-08) |
| 5 | 転送量制限 | 転送量制限なし（著しい高負荷時は帯域制限の場合あり） [公式](https://manual.sakura.ad.jp/vps/support/technical/resource-limit.html)<br>(2026-07-08) | 転送量制限なし（ベストエフォート） [公式](https://support.conoha.jp/vps/faq/vps-q/)<br>(2026-07-08) | 転送量制限なし（ベストエフォート） [公式](https://vps.xserver.ne.jp/xserver-vps.php)<br>(2026-07-08) | 無制限 [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | 無制限 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-07) |
| 6 | 帯域目安（Gbps） | 不明 | 不明 | 不明 | 1 [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | 不明 |
| 7 | ローカルネットワーク | ✅ [公式](https://manual.sakura.ad.jp/vps/network/index.html)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/privatenetwork/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/vps/manual/index.php?action=artikel&cat=55&id=130)<br>(2026-07-08) |
| 8 | プライベートネットワーク | ✅ [公式](https://manual.sakura.ad.jp/vps/network/localnetwork.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/v/privatenetwork/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/vps/charge/index.html)<br>(2026-07-07) |
| 9 | VLAN | ✅ [公式](https://manual.sakura.ad.jp/vps/network/index.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/v/privatenetwork/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 10 | ロードバランサー | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/vps/charge/index.html)<br>(2026-07-07) |
| 11 | Floating IP | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/vps/manual/index.php?action=artikel&cat=18&id=69)<br>(2026-07-07) |

## セキュリティ

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SSH鍵ログイン | 不明 | 不明 | 不明 | 不明 | 不明 |
| 2 | ファイアウォール機能 | ✅ [公式](https://vps.sakura.ad.jp/feature/packetfilter.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/v/v3-security-securitygroup/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/feature/security/)<br>(2026-07-08) |
| 3 | DDoS保護 | なし（パケットフィルター機能のみ） [公式](https://manual.sakura.ad.jp/vps/network/packetfilter.html)<br>(2026-07-08) | あり（DDoS攻撃対策システムを標準搭載） [公式](https://vps.conoha.jp/features/)<br>(2026-07-08) | あり（グローバル規模のDDoS対策システム標準提供） [公式](https://vps.xserver.ne.jp/support/news_detail.php?view_id=15098)<br>(2026-07-08) | なし（Indigo VPS向けのDDoS保護は提供されていない） [公式](https://web.arena.ne.jp/indigo/spec/security.html)<br>(2026-07-08) | 不明 |
| 4 | WAF | ✅ [公式](https://manual.sakura.ad.jp/vps/server/siteguard/)<br>(2026-07-08) | ❌ [公式](https://support.conoha.jp/vps/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/security.html)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/feature/security/)<br>(2026-07-08) |
| 5 | セキュリティグループ | ✅ [公式](https://vps.sakura.ad.jp/feature/packetfilter.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/v/v3-security-securitygroup/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/feature/security/)<br>(2026-07-08) |
| 6 | 二要素認証（管理画面） | ✅ [公式](https://manual.sakura.ad.jp/vps/controlpanel/index.html)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/)<br>(2026-07-08) |
| 7 | APIトークン | ✅ [公式](https://manual.sakura.ad.jp/vps/api/)<br>(2026-07-08) | ✅ [公式](https://www.conoha.jp/vps/function/api/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 8 | IAM / 権限管理 | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://support.conoha.jp/vps/faq/api-q/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 9 | 監査ログ | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://support.conoha.jp/vps/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 10 | ISO27001 | True [公式](https://www.sakura.ad.jp/corporate/security/)<br>(2026-07-08) | 不明 | True [公式](https://www.xserver.ne.jp/news_detail.php?view_id=9765)<br>(2026-07-08) | True [公式](https://web.arena.ne.jp/)<br>(2026-07-08) | True [公式](https://www.kagoya.jp/securitypolicy/)<br>(2026-07-08) |
| 11 | ISMS | True [公式](https://www.sakura.ad.jp/corporate/security/)<br>(2026-07-08) | 不明 | True [公式](https://www.xserver.ne.jp/news_detail.php?view_id=9765)<br>(2026-07-08) | True [公式](https://web.arena.ne.jp/)<br>(2026-07-08) | True [公式](https://www.kagoya.jp/securitypolicy/)<br>(2026-07-08) |
| 12 | SOC 2 | True [公式](https://www.sakura.ad.jp/corporate/security/)<br>(2026-07-08) | 不明 | 不明 | 不明 | 不明 |
| 13 | PCI DSS | True [公式](https://www.sakura.ad.jp/corporate/security/)<br>(2026-07-08) | 不明 | 不明 | 不明 | 不明 |
| 14 | データセンター認証 | 不明 | 不明 | 不明 | 不明 | 不明 |

## バックアップ / イメージ保存

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 手動バックアップ | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/snapshot/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_image.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 2 | 自動バックアップ | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 3 | バックアップスケジュール設定 | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ❌ [公式](https://doc.conoha.jp/products/vps-v3/storage-v3/autobackup-v3/)<br>(2026-07-07) | ❌ [公式](https://vps.xserver.ne.jp/business.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/option/backup/)<br>(2026-07-08) |
| 4 | バックアップ保持期間 | N/A（バックアップ機能なし） [公式](https://vps.sakura.ad.jp/faq/)<br>(2026-07-08) | 最大30世代（日次バックアップ） [公式](https://vps.conoha.jp/function/autobk/)<br>(2026-07-08) | 1世代（1週間）、オプションで最大3世代 [公式](https://vps.xserver.ne.jp/support/manual/man_server_auto_backup_gene.php)<br>(2026-07-08) | 最大5個（スナップショット） [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | Liteプラン：1世代、Proプラン：世代数無制限（有料オプション） [公式](https://www.kagoya.jp/option/backup/)<br>(2026-07-08) |
| 5 | バックアップ世代数 | 0 [公式](https://vps.sakura.ad.jp/faq/)<br>(2026-07-08) | 14世代（デフォルト）、最大30世代（VPS 3.0） [公式](https://doc.conoha.jp/products/vps-v3/storage-v3/autobackup-v3/)<br>(2026-07-07) | ビジネスプラン標準1世代、バックアップ拡張オプションで最大3世代 [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | 最大5個/インスタンス（スナップショット） [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | 最大7世代（定期スナップショット） [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 6 | バックアップからの復元 | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/business.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 7 | バックアップ暗号化 | ❌ [公式](https://vps.sakura.ad.jp/faq/)<br>(2026-07-08) | ❌ [公式](https://vps.conoha.jp/function/autobk/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/business.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 8 | オブジェクトストレージへのバックアップ | ❌ [公式](https://vps.sakura.ad.jp/faq/)<br>(2026-07-08) | ❌ [公式](https://vps.conoha.jp/function/autobk/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/business.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 9 | リージョン間バックアップ | ❌ [公式](https://vps.sakura.ad.jp/faq/)<br>(2026-07-08) | ❌ [公式](https://vps.conoha.jp/function/autobk/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/business.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 10 | DR（災害復旧）対応 | なし [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | なし [公式](https://vps.conoha.jp/function/)<br>(2026-07-08) | なし [公式](https://vps.xserver.ne.jp/business.php)<br>(2026-07-08) | なし [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | なし [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 11 | バックアップ課金 | 有料オプション（Acronis Cyber Protect Cloud: 1,760円/月〜(100GB)） [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | 有料オプション（世代数により料金変動） [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ビジネスプラン料金に含む（追加世代は有料オプション） [公式](https://vps.xserver.ne.jp/support/manual/man_server_auto_backup_gene.php)<br>(2026-07-08) | 有料オプション [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | 有料（容量課金：スナップショット10GBあたり日額4.4円） [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |

## API / CLI / Terraform

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | REST API | ✅ [公式](https://manual.sakura.ad.jp/vps/api/)<br>(2026-07-07) | ✅ [公式](https://www.conoha.jp/vps/function/api/)<br>(2026-07-07) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 2 | OpenAPI公開 | ✅ [公式](https://manual.sakura.ad.jp/vps/api/api-doc/index.html)<br>(2026-07-07) | ✅ [公式](https://github.com/gmo-internet/conoha_vps_openapi)<br>(2026-07-07) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 3 | CLI | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ✅ [公式](https://doc.conoha.jp/reference/openstack-cli/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 4 | Terraform Provider | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ✅ [公式](https://vps.conoha.jp/terraform_provider/)<br>(2026-07-07) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 5 | Pulumi対応 | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://registry.pulumi.com/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 6 | Ansible対応 | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 7 | メタデータサービス | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 8 | APIレート制限公開 | ✅ [公式](https://manual.sakura.ad.jp/vps/api/api-doc/index.html)<br>(2026-07-07) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 9 | Webhook | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 10 | SDK（Go） | ❌ [公式](https://manual.sakura.ad.jp/vps/api/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 11 | SDK（Python） | ❌ [公式](https://manual.sakura.ad.jp/vps/api/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |
| 12 | SDK（Node.js） | ❌ [公式](https://manual.sakura.ad.jp/vps/api/)<br>(2026-07-08) | ❌ [公式](https://doc.conoha.jp/reference/)<br>(2026-07-08) | ❌ [公式](https://vps.xserver.ne.jp/feature.php)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-08) | ❌ [公式](https://www.kagoya.jp/vps/function-plan/)<br>(2026-07-08) |

## サポート / SLA

| # | 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SLA稼働率（%） | 99.99 [公式](https://vps.sakura.ad.jp/agreement/)<br>(2024-01-01) | 99.99 [公式](https://www.conoha.jp/vps/agreement/)<br>(2024-01-01) | 99.99 [公式](https://vps.xserver.ne.jp/agreement/)<br>(2024-01-01) | 不明 | 99.999 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-08) |
| 2 | SLA文書URL | https://vps.sakura.ad.jp/agreement/ [公式](https://vps.sakura.ad.jp/agreement/)<br>(2026-07-08) | https://www.conoha.jp/vps/agreement/ [公式](https://www.conoha.jp/vps/agreement/)<br>(2026-07-08) | https://vps.xserver.ne.jp/support/manual/man_order_sla.php [公式](https://vps.xserver.ne.jp/support/manual/man_order_sla.php)<br>(2026-07-08) | なし（Indigo VPS向けSLAは提供されていない） [公式](https://web.arena.ne.jp/indigo/)<br>(2026-07-08) | 不明 |
| 3 | ステータスページ | ✅ [公式](https://www.sakura.ad.jp/status/)<br>(2026-07-08) | ✅ [公式](https://status.conoha.jp/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/information/)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/info/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/news/)<br>(2026-07-08) |
| 4 | 障害情報ページ | ✅ [公式](https://support.sakura.ad.jp/mainte/)<br>(2026-07-08) | ✅ [公式](https://www.conoha.jp/news/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/information/)<br>(2026-07-08) | ✅ [公式](https://help.arena.ne.jp/hc/ja/sections/900000494023)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/news/)<br>(2026-07-08) |
| 5 | メンテナンス情報ページ | ✅ [公式](https://support.sakura.ad.jp/mainte/)<br>(2026-07-08) | ✅ [公式](https://www.conoha.jp/news/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/information/)<br>(2026-07-08) | ✅ [公式](https://help.arena.ne.jp/hc/ja/sections/900000494023)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/news/)<br>(2026-07-08) |
| 6 | メール通知 | ✅ [公式](https://help.sakura.ad.jp/)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/)<br>(2026-07-08) |
| 7 | サポート窓口 | メール・チャット・電話（コールバック） [公式](https://help.sakura.ad.jp/)<br>(2026-07-08) | メール・チャット [公式](https://support.conoha.jp/help/contact/)<br>(2026-07-08) | メール・チャット・電話 [公式](https://vps.xserver.ne.jp/support/)<br>(2026-07-08) | メール [公式](https://web.arena.ne.jp/indigo/support/)<br>(2026-07-08) | メール・チャット・電話 [公式](https://www.kagoya.jp/support/)<br>(2026-07-08) |
| 8 | 電話サポート | ✅ [公式](https://help.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://support.conoha.jp/help/contact/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/support/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/support/)<br>(2026-07-08) |
| 9 | チャットサポート | ✅ [公式](https://help.sakura.ad.jp/purpose_beginner/2580/)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/help/contact/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/)<br>(2026-07-08) | ❌ [公式](https://web.arena.ne.jp/indigo/support/)<br>(2026-07-08) | ✅ [公式](https://webchat.kagoya.jp/)<br>(2026-07-08) |
| 10 | 問い合わせフォーム | ✅ [公式](https://help.sakura.ad.jp/contact/)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/inquiry/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/support/indigo/)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/contact/)<br>(2026-07-08) |
| 11 | 法人向けサポート | ❌ [公式](https://vps.sakura.ad.jp/)<br>(2026-07-08) | ❌ [公式](https://support.conoha.jp/vps/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/business.php)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigopro/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/vps/)<br>(2026-07-08) |
| 12 | 日本語サポート | ✅ [公式](https://help.sakura.ad.jp/)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/indigo/support/)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/support/)<br>(2026-07-08) |
| 13 | ナレッジベース / FAQ | ✅ [公式](https://help.sakura.ad.jp/)<br>(2026-07-08) | ✅ [公式](https://support.conoha.jp/vps/guide/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/)<br>(2026-07-08) | ✅ [公式](https://web.arena.ne.jp/support/indigo/faq/index.html)<br>(2026-07-08) | ✅ [公式](https://support.kagoya.jp/vps/manual/)<br>(2026-07-08) |

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
