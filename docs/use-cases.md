# 用途別 VPS 比較

> このファイルは `scripts/generate_docs.py` により自動生成されています。手動で編集しないでください。
> 「不明」は公式情報が確認できないことを示します。推測によるおすすめ順位付けは行っていません。

## 低価格重視

> 初期費用・月額料金を抑えたい場合の比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| 最低月額料金（円） | 643 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 460 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1496 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 319 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 550 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 2GBプラン月額（円・税込） | 1738 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 1259 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1496 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 814 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 770 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 2GBプラン時間課金（円/時・税込） | - [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 3.7 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 1.27 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | - [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 4GBプラン月額（円・税込） | 3520 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 2189 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 1630 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 1760 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 4GBプラン時間課金（円/時・税込） | - [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 6.6 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 2.55 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | - [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 月額上限（円・税込） | - [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 751 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | - [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 319 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 550 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 初期費用（円・税込） | 0 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 0 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 0 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 0 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 0 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 最低利用期間 | 1ヶ月 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | なし [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1ヶ月 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | なし [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | なし [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |

## 開発・検証環境

> 開発・検証用途で重要な自動化・スクリプト・スナップショット等の比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| スタートアップスクリプト | 不明 | 不明 | 不明 | 不明 | 不明 |
| cloud-init明記 | 不明 | 不明 | 不明 | 不明 | 不明 |
| Docker系テンプレート | 不明 | 不明 | 不明 | 不明 | 不明 |
| カスタムISO | 不明 | 不明 | 不明 | 不明 | 不明 |
| REST API | ✅ [🔗](https://manual.sakura.ad.jp/vps/api/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/function/api/) (2024-01-01) | 不明 | 不明 | 不明 |
| CLI | 不明 | 不明 | 不明 | 不明 | 不明 |
| Terraform Provider | 不明 | 不明 | 不明 | 不明 | 不明 |
| SSH鍵ログイン | 不明 | 不明 | 不明 | 不明 | 不明 |
| スナップショット | ✅ [🔗](https://vps.sakura.ad.jp/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/function/) (2024-01-01) | 不明 | 不明 | 不明 |
| 自動スナップショット | 不明 | 不明 | 不明 | 不明 | 不明 |

## WordPress / Webサイト運用

> WordPressやWebサイト運用に関連する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| アプリテンプレート | 不明 | 不明 | 不明 | 不明 | 不明 |
| KUSANAGIテンプレート | 不明 | 不明 | 不明 | 不明 | 不明 |
| 最低月額料金（円） | 643 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 460 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1496 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 319 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 550 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| 2GBプラン月額（円・税込） | 1738 [🔗](https://vps.sakura.ad.jp/specification/) (2026-07-03) | 1259 [🔗](https://www.conoha.jp/vps/pricing/) (2026-07-03) | 1496 [🔗](https://vps.xserver.ne.jp/price/) (2026-07-03) | 814 [🔗](https://web.arena.ne.jp/indigo/price/) (2026-07-03) | 770 [🔗](https://www.kagoya.jp/vps/) (2026-07-03) |
| バックアップ機能 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 自動バックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| スナップショット | ✅ [🔗](https://vps.sakura.ad.jp/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/function/) (2024-01-01) | 不明 | 不明 | 不明 |
| ファイアウォール機能 | 不明 | 不明 | 不明 | 不明 | 不明 |
| DDoS保護 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ロードバランサー | 不明 | 不明 | 不明 | 不明 | 不明 |
| SLA稼働率（%） | 99.99 [🔗](https://vps.sakura.ad.jp/agreement/) (2024-01-01) | 99.99 [🔗](https://www.conoha.jp/vps/agreement/) (2024-01-01) | 99.99 [🔗](https://vps.xserver.ne.jp/agreement/) (2024-01-01) | 不明 | 不明 |

## 本番サービス運用

> 本番環境での安定稼働・冗長性・セキュリティに関する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| SLA稼働率（%） | 99.99 [🔗](https://vps.sakura.ad.jp/agreement/) (2024-01-01) | 99.99 [🔗](https://www.conoha.jp/vps/agreement/) (2024-01-01) | 99.99 [🔗](https://vps.xserver.ne.jp/agreement/) (2024-01-01) | 不明 | 不明 |
| SLA文書URL | 不明 | 不明 | 不明 | 不明 | 不明 |
| ロードバランサー | 不明 | 不明 | 不明 | 不明 | 不明 |
| プライベートネットワーク | 不明 | 不明 | 不明 | 不明 | 不明 |
| 自動バックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップ保持期間 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ファイアウォール機能 | 不明 | 不明 | 不明 | 不明 | 不明 |
| DDoS保護 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ステータスページ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 障害情報ページ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 国内リージョン数 | 不明 | 不明 | 不明 | 不明 | 不明 |
| 複数リージョン構成 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ISO27001 | 不明 | 不明 | 不明 | 不明 | 不明 |
| ISMS | 不明 | 不明 | 不明 | 不明 | 不明 |

## バックアップ・DR重視

> バックアップ・障害復旧（DR）対応に関する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| 手動バックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| 自動バックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップスケジュール設定 | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップ保持期間 | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップ世代数 | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップからの復元 | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップ暗号化 | 不明 | 不明 | 不明 | 不明 | 不明 |
| オブジェクトストレージへのバックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| リージョン間バックアップ | 不明 | 不明 | 不明 | 不明 | 不明 |
| DR（災害復旧）対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| スナップショット | ✅ [🔗](https://vps.sakura.ad.jp/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/function/) (2024-01-01) | 不明 | 不明 | 不明 |
| 自動スナップショット | 不明 | 不明 | 不明 | 不明 | 不明 |
| バックアップ課金 | 不明 | 不明 | 不明 | 不明 | 不明 |

## API / IaC による自動化重視

> REST API・CLI・Terraform等の自動化ツール対応に関する比較項目です。

| 項目 | さくらのVPS | ConoHa VPS | Xserver VPS | WebARENA Indigo | KAGOYA CLOUD VPS |
| --- | --- | --- | --- | --- | --- |
| REST API | ✅ [🔗](https://manual.sakura.ad.jp/vps/api/) (2024-01-01) | ✅ [🔗](https://www.conoha.jp/vps/function/api/) (2024-01-01) | 不明 | 不明 | 不明 |
| OpenAPI公開 | 不明 | 不明 | 不明 | 不明 | 不明 |
| CLI | 不明 | 不明 | 不明 | 不明 | 不明 |
| Terraform Provider | 不明 | 不明 | 不明 | 不明 | 不明 |
| Pulumi対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| Ansible対応 | 不明 | 不明 | 不明 | 不明 | 不明 |
| メタデータサービス | 不明 | 不明 | 不明 | 不明 | 不明 |
| APIレート制限公開 | 不明 | 不明 | 不明 | 不明 | 不明 |
| Webhook | 不明 | 不明 | 不明 | 不明 | 不明 |
| SDK（Go） | 不明 | 不明 | 不明 | 不明 | 不明 |
| SDK（Python） | 不明 | 不明 | 不明 | 不明 | 不明 |
| SDK（Node.js） | 不明 | 不明 | 不明 | 不明 | 不明 |
| スタートアップスクリプト | 不明 | 不明 | 不明 | 不明 | 不明 |
| cloud-init明記 | 不明 | 不明 | 不明 | 不明 | 不明 |

## 凡例

| 表示 | 意味 |
| --- | --- |
| ✅ | 対応あり（確認済み） |
| ❌ | 非対応（確認済み） |
| `-` | プランなし・該当なし（確認済み） |
| 不明 | 公式情報が確認できていない |

> 値の表現ルールの詳細は [docs/data-policy.md](data-policy.md) を参照してください。
