# Copilot Instructions

## プロジェクトの目的

国内VPSリファレンスを作成する。

## 基本方針

- 公式情報優先
- 推測禁止
- unknownを許可
- VPSとCloudを混同しない

## AI作業方針

- Issue の内容を最優先する
- 公式情報の実収集は、Issueで明示されている場合のみ行う
- 値を推測して追加しない
- 不明な値は unknown とする
- 既存の YAML 構造との互換性をできるだけ保つ
- YAML を変更した場合は docs を再生成する
- GitHub Actions が成功する状態で PR を作成する

## データ構造

YAMLが正

Markdownは生成物

## Evidence / Source 管理

- 比較値には可能な限り情報源メタデータを持たせる
- source_type は official / benchmark / manual / community / unknown のいずれかを使う
- source_url が確認できない場合は unknown を使う
- verified_at が確認できない場合は unknown を使う
- verification_status は verified / unverified / unknown のいずれかを使う
- 公式情報と第三者情報・ベンチマーク情報を混同しない

## PR作成ルール

- docs は生成物として扱い、YAML変更時にのみ再生成結果を反映する
- GitHub Actions が成功していることを確認してから PR を作成する

## コーディング

Python 3.12

PEP8

## ドキュメント

日本語
