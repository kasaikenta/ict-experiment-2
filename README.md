# 情報通信実験第2 — 情報理論・符号理論

講義資料の掲載先：**https://kasai.ict.eng.isct.ac.jp/ict-e218/**

2026-11-14、ほかの講義と同じく、大学HP内の科目別ディレクトリに講義PDFを配置し、直接リンクする形式へ変更しました。従来のGitHub Pagesの入口は上記へ転送します。

**2026年度の課題PDF・新版入力データ・教員用解答は引き続き非公開です。このリポジトリやHPの公開領域に追加しないでください。** 体験型教材も掲載対象外です。提出方法は従来どおり、授業で指定するシステムへの電子提出です。

## HP側の構成

```text
www/ict-e218/
  index.html
  lectures/
    information-01.pdf
    information-02.pdf
    coding.pdf
```

HPのトップページ（index.html、en.html）のTeaching欄から科目ページへリンクしています。公開ページのHTML原稿は`web/index.html`、講義PDFは`lectures/`に保存しています。

## 今後の更新

1. HTMLは`web/index.html`、講義資料は元のLaTeX等のソースで修正する。
2. PDFを再生成した場合は日本語フォントの埋め込みと全ページの表示を確認する。
3. `kasai-www`のSFTP接続で対象の現在版を取得し、変更がないことを確認してからバックアップを保存する。
4. HTMLは`www/ict-e218/index.html`、PDFは対応する`www/ict-e218/lectures/`へアップロードする。
5. 配置後に読み戻したファイルとローカル原稿のハッシュを照合し、公開URLを確認する。

URLは更新後も同じものを使用します。課題資料の公開再開は、教員の明示的な指示後に行います。

## 従来の配布版

`materials/`と`downloads/`には従来公開済みのサンプル・入力データ・版番号付きZIPを保持しています。今年度の新版入力データではありません。

`release.json`の`homepage`は現在の大学HPのURL、`assignments_public`は`false`です。`tools/build_site.py`は従来の配布ZIPを保ち、GitHub Pagesの入口を大学HPへ転送するHTMLを生成します。既存の公開済みZIPを変更する場合は新しい版番号を使用してください。
