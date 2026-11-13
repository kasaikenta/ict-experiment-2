# 情報通信実験第2 — 情報理論・符号理論

講義資料への入口：**https://kasai.ict.eng.isct.ac.jp/#teaching**

2026-11-14、講義PDF3本をLaTeXで再構成した改訂版へ差し替えました。大学HPトップのTeaching欄から各PDFへ直接リンクしています。`ict-e218/`はファイル置き場専用で、内容ページは設けません。従来のGitHub Pagesの入口はHPトップのTeaching欄へ転送します。

**2026年度の課題PDF・新版入力データ・教員用解答は引き続き非公開です。このリポジトリやHPの公開領域に追加しないでください。** 体験型教材も掲載対象外です。提出方法は従来どおり、授業で指定するシステムへの電子提出です。

## 講義PDF

- [情報理論・前半（26ページ）](https://kasai.ict.eng.isct.ac.jp/ict-e218/lectures/information-01.pdf)
- [情報理論・後半（29ページ）](https://kasai.ict.eng.isct.ac.jp/ict-e218/lectures/information-02.pdf)
- [符号理論・前半＋後半（64ページ）](https://kasai.ict.eng.isct.ac.jp/ict-e218/lectures/coding.pdf)

## HP側の構成

```text
www/index.html, www/en.html   Teaching欄に各PDFへの直接リンク
www/ict-e218/lectures/
  information-01.pdf
  information-02.pdf
  coding.pdf
```

`www/ict-e218/index.html`は置きません。このリポジトリの`lectures/`には現在の公開PDFを保存しています。

## 今後の更新

1. 講義資料の元のLaTeXソースを修正し、PDFを再生成する。
2. 日本語フォントの埋め込みと全ページの表示を確認する。
3. `kasai-www`のSFTP接続で対象の現在版を取得し、変更がないことを確認してからバックアップを保存する。
4. 対応する`www/ict-e218/lectures/`のPDFを差し替える。
5. 読み戻したファイルとローカル原稿のハッシュを照合し、公開URLを確認する。
6. このリポジトリの`lectures/`も同じPDFに更新する。

URLは更新後も同じものを使用します。課題資料の公開再開は、教員の明示的な指示後に行います。

## 従来の配布版

`materials/`と`downloads/`には従来公開済みのサンプル・入力データ・版番号付きZIPを保持しています。今年度の新版入力データではありません。既存ZIPは過去の版として保存し、今回の講義改訂では変更していません。最新版の講義PDFは上記の直接リンクから取得してください。

`release.json`の版番号・日付は従来のZIP配布版を表し、`homepage`はHPの講義資料欄、`assignments_public`は`false`です。`tools/build_site.py`で新しいZIPを作る場合は、先に版番号・タグ・日付を更新してください。同じ版番号の公開済みZIPは上書きできません。
