# 用途別 VPS 比較

> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。
> 「不明」は公式情報が確認できないことを示します。推測によるおすすめ順位付けは行っていません。

## 低価格重視

> 初期費用・月額料金を抑えたい場合の比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| 最低月額料金（円） | 643 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 460 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1496 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 319 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 550 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 2GBプラン月額（円・税込） | 1738 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 1259 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1496 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 814 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 770 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 2GBプラン時間課金（円/時・税込） | - [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 3.7 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 1.27 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | - [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 4GBプラン月額（円・税込） | 3520 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 2189 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 1630 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 1760 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 4GBプラン時間課金（円/時・税込） | - [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 6.6 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 2.55 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | - [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 月額上限（円・税込） | - [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 751 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | - [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 319 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 550 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 初期費用（円・税込） | 0 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 0 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 0 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 0 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 0 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 最低利用期間 | 1ヶ月 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | なし [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1ヶ月 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | なし [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | なし [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |

## 開発・検証環境

> 開発・検証用途で重要な自動化・スクリプト・スナップショット等の比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| スタートアップスクリプト | ✅ [公式](https://manual.sakura.ad.jp/vps/startupscript/startupscript.html)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/startupscript/)<br>(2026-07-07) | 不明 | 不明 | ✅ [公式](https://www.kagoya.jp/cloud/vps/manual/instance/)<br>(2026-07-07) |
| cloud-init明記 | 不明 | 不明 | 不明 | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/cloud/vps/manual/instance/)<br>(2026-07-07) |
| Docker系テンプレート | ✅ [公式](https://vps.sakura.ad.jp/specification/#specification_application)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/os-list.php)<br>(2026-07-07) | 不明 | 不明 |
| カスタムISO | ✅ [公式](https://manual.sakura.ad.jp/vps/os-reinstall/iso-install.html)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/vps/iso-upload/)<br>(2026-07-07) | 不明 | 不明 | ✅ [公式](https://www.kagoya.jp/support/category/cloud/vps/vps_manual/iso/)<br>(2026-07-07) |
| REST API | ✅ [公式](https://manual.sakura.ad.jp/vps/api/)<br>(2026-07-07) | ✅ [公式](https://www.conoha.jp/vps/function/api/)<br>(2026-07-07) | 不明 | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | 不明 |
| CLI | 不明 | 不明 | 不明 | 不明 | 不明 |
| Terraform Provider | 不明 | ✅ [公式](https://vps.conoha.jp/terraform_provider/)<br>(2026-07-07) | 不明 | 不明 | 不明 |
| SSH鍵ログイン | 不明 | 不明 | 不明 | 不明 | 不明 |
| スナップショット | ✅ [公式](https://vps.sakura.ad.jp/)<br>(2024-01-01) | ✅ [公式](https://www.conoha.jp/vps/function/)<br>(2024-01-01) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_image.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 自動スナップショット | 不明 | ❌ [公式](https://support.conoha.jp/v/snapshot/)<br>(2026-07-07) | 不明 | 不明 | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |

## WordPress / Webサイト運用

> WordPressやWebサイト運用に関連する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| アプリテンプレート | ✅ [公式](https://vps.sakura.ad.jp/specification/#specification_application)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/os-list.php)<br>(2026-07-07) | 不明 | 不明 |
| KUSANAGIテンプレート | ✅ [公式](https://vps.sakura.ad.jp/specification/#specification_application)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/template/?btn_id=top--function_function-template)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_app_use_kusanagi.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/kusanagi.html)<br>(2026-07-07) | 不明 |
| 最低月額料金（円） | 643 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 460 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1496 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 319 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 550 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| 2GBプラン月額（円・税込） | 1738 [公式](https://vps.sakura.ad.jp/specification/)<br>(2026-07-03) | 1259 [公式](https://www.conoha.jp/vps/pricing/)<br>(2026-07-03) | 1496 [公式](https://vps.xserver.ne.jp/price/)<br>(2026-07-03) | 814 [公式](https://web.arena.ne.jp/indigo/price/)<br>(2026-07-03) | 770 [公式](https://www.kagoya.jp/vps/)<br>(2026-07-03) |
| バックアップ機能 | ✅ [公式](https://vps.sakura.ad.jp/feature/backup/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | 不明 | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 自動バックアップ | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | 不明 | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| スナップショット | ✅ [公式](https://vps.sakura.ad.jp/)<br>(2024-01-01) | ✅ [公式](https://www.conoha.jp/vps/function/)<br>(2024-01-01) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_image.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| ファイアウォール機能 | 不明 | 不明 | 不明 | 不明 | 不明 |
| DDoS保護 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ロードバランサー | 不明 | 不明 | 不明 | 不明 | ✅ [公式](https://support.kagoya.jp/vps/charge/index.html)<br>(2026-07-07) |
| SLA稼働率（%） | 99.99 [公式](https://vps.sakura.ad.jp/agreement/)<br>(2024-01-01) | 99.99 [公式](https://www.conoha.jp/vps/agreement/)<br>(2024-01-01) | 99.99 [公式](https://vps.xserver.ne.jp/agreement/)<br>(2024-01-01) | 不明 | 不明 |

## 本番サービス運用

> 本番環境での安定稼働・冗長性・セキュリティに関する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| SLA稼働率（%） | 99.99 [公式](https://vps.sakura.ad.jp/agreement/)<br>(2024-01-01) | 99.99 [公式](https://www.conoha.jp/vps/agreement/)<br>(2024-01-01) | 99.99 [公式](https://vps.xserver.ne.jp/agreement/)<br>(2024-01-01) | 不明 | 不明 |
| SLA文書URL | 不明 | 不明 | 不明 | 不明 | 不明 |
| ロードバランサー | 不明 | 不明 | 不明 | 不明 | ✅ [公式](https://support.kagoya.jp/vps/charge/index.html)<br>(2026-07-07) |
| プライベートネットワーク | 不明 | 不明 | 不明 | 不明 | ✅ [公式](https://support.kagoya.jp/vps/charge/index.html)<br>(2026-07-07) |
| 自動バックアップ | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | 不明 | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| バックアップ保持期間 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ファイアウォール機能 | 不明 | 不明 | 不明 | 不明 | 不明 |
| DDoS保護 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ステータスページ | ✅ [公式](https://www.sakura.ad.jp/status/)<br>(2026-07-08) | 不明 | 不明 | 不明 | 不明 |
| 障害情報ページ | ✅ [公式](https://support.sakura.ad.jp/mainte/)<br>(2026-07-08) | ✅ [公式](https://www.conoha.jp/news/)<br>(2026-07-08) | ✅ [公式](https://vps.xserver.ne.jp/support/information/)<br>(2026-07-08) | ✅ [公式](https://help.arena.ne.jp/hc/ja/sections/900000494023)<br>(2026-07-08) | ✅ [公式](https://www.kagoya.jp/news/)<br>(2026-07-08) |
| 国内リージョン数 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 複数リージョン構成 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ISO27001 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ISMS | 不明 | 不明 | 不明 | 不明 | 不明 |

## バックアップ・DR重視

> バックアップ・障害復旧（DR）対応に関する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| 手動バックアップ | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/snapshot/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_image.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 自動バックアップ | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | ✅ [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | 不明 | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| バックアップスケジュール設定 | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ❌ [公式](https://doc.conoha.jp/products/vps-v3/storage-v3/autobackup-v3/)<br>(2026-07-07) | 不明 | 不明 | 不明 |
| バックアップ保持期間 | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップ世代数 | 不明 | 14世代（デフォルト）、最大30世代（VPS 3.0） [公式](https://doc.conoha.jp/products/vps-v3/storage-v3/autobackup-v3/)<br>(2026-07-07) | ビジネスプラン標準1世代、バックアップ拡張オプションで最大3世代 [公式](https://vps.xserver.ne.jp/support/faq/service_server_backup.php)<br>(2026-07-07) | 最大5個/インスタンス（スナップショット） [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | 最大7世代（定期スナップショット） [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| バックアップからの復元 | ✅ [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | ✅ [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | 不明 | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| バックアップ暗号化 | 不明 | 不明 | 不明 | 不明 | 不明 |
| オブジェクトストレージへのバックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| リージョン間バックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| DR（災害復旧）対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| スナップショット | ✅ [公式](https://vps.sakura.ad.jp/)<br>(2024-01-01) | ✅ [公式](https://www.conoha.jp/vps/function/)<br>(2024-01-01) | ✅ [公式](https://vps.xserver.ne.jp/support/manual/man_server_image.php)<br>(2026-07-07) | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| 自動スナップショット | 不明 | ❌ [公式](https://support.conoha.jp/v/snapshot/)<br>(2026-07-07) | 不明 | 不明 | ✅ [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |
| バックアップ課金 | 有料オプション（Acronis Cyber Protect Cloud: 1,760円/月〜(100GB)） [公式](https://vps.sakura.ad.jp/contents/info/acronis-cyber-protect-cloud-acronis-hosted/)<br>(2026-07-07) | 有料オプション（世代数により料金変動） [公式](https://support.conoha.jp/v/vps-autobackup/)<br>(2026-07-07) | 不明 | 不明 | 有料（容量課金：スナップショット10GBあたり日額4.4円） [公式](https://www.kagoya.jp/vps/feature/customize/)<br>(2026-07-07) |

## API / IaC による自動化重視

> REST API・CLI・Terraform等の自動化ツール対応に関する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| REST API | ✅ [公式](https://manual.sakura.ad.jp/vps/api/)<br>(2026-07-07) | ✅ [公式](https://www.conoha.jp/vps/function/api/)<br>(2026-07-07) | 不明 | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | 不明 |
| OpenAPI公開 | ✅ [公式](https://manual.sakura.ad.jp/vps/api/api-doc/index.html)<br>(2026-07-07) | ✅ [公式](https://github.com/gmo-internet/conoha_vps_openapi)<br>(2026-07-07) | 不明 | 不明 | 不明 |
| CLI | 不明 | 不明 | 不明 | 不明 | 不明 |
| Terraform Provider | 不明 | ✅ [公式](https://vps.conoha.jp/terraform_provider/)<br>(2026-07-07) | 不明 | 不明 | 不明 |
| Pulumi対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| Ansible対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| メタデータサービス | 不明 | 不明 | 不明 | 不明 | 不明 |
| APIレート制限公開 | ✅ [公式](https://manual.sakura.ad.jp/vps/api/api-doc/index.html)<br>(2026-07-07) | 不明 | 不明 | 不明 | 不明 |
| Webhook | 不明 | 不明 | 不明 | 不明 | 不明 |
| SDK（Go） | 不明 | 不明 | 不明 | 不明 | 不明 |
| SDK（Python） | 不明 | 不明 | 不明 | 不明 | 不明 |
| SDK（Node.js） | 不明 | 不明 | 不明 | 不明 | 不明 |
| スタートアップスクリプト | ✅ [公式](https://manual.sakura.ad.jp/vps/startupscript/startupscript.html)<br>(2026-07-07) | ✅ [公式](https://vps.conoha.jp/function/startupscript/)<br>(2026-07-07) | 不明 | 不明 | ✅ [公式](https://www.kagoya.jp/cloud/vps/manual/instance/)<br>(2026-07-07) |
| cloud-init明記 | 不明 | 不明 | 不明 | ✅ [公式](https://web.arena.ne.jp/indigo/spec/)<br>(2026-07-07) | ✅ [公式](https://www.kagoya.jp/cloud/vps/manual/instance/)<br>(2026-07-07) |

## 凡例

| 表示 | 意味 |
| --- | --- |
| ✅ | 対応あり（確認済み） |
| ❌ | 非対応（確認済み） |
| `-` | プランなし・該当なし（確認済み） |
| 不明 | 公式情報が確認できていない |

> 値の表現ルールの詳細は [docs/data-policy.md](data-policy.md) を参照してください。
