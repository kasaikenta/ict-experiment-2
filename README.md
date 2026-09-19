# 情報通信実験第2 — 情報理論・符号理論

教材ページ：**https://kasaikenta.github.io/ict-experiment-2/**

授業スライド・課題・サンプルプログラム・入力データを公開しています。

## 学生の方へ

1. 教材ページで課題PDFを開いてください。
2. 対応する「プログラム・入力データ」をZIPでダウンロードし、展開してください。GitやGitHubアカウントは不要です。
3. 「授業スライド」欄から各講義のPDFを閲覧・ダウンロードできます。
4. プログラムとレポートは、授業で指定されたシステムに電子データで提出してください。提出期限・形式は授業内およびシステム上の案内に従ってください。

C言語サンプルは穴埋め用です。`// ???` は各自で実装してください。

## 更新と版管理

- 教材トップページのURLは固定です。
- 現在の配付版は `release.json` と教材ページに表示しています。
- 各版のZIPは [Releases](https://github.com/kasaikenta/ict-experiment-2/releases) に保存します。通常の更新では古い版のタグ・ZIPを上書きしません。公開終了の対象を含む版は取り下げます。
- 変更点は [CHANGELOG.md](CHANGELOG.md) に記録します。
- 授業中に配付版を変更する場合は、授業システムでも変更内容を案内してください。

## 教員向け：更新手順

1. 対象のPDF・Cソース・入力データを修正する。
2. 教材内容を変更する場合は `release.json` のversion・tagを新しい値（例：`2026-v2`）にし、dateを更新する。
3. `CHANGELOG.md` に変更点を追記する。
4. `python3 tools/build_site.py` を実行する。既存の版のZIPが変わる場合はエラーになるため、新しい版番号を使う。
5. 変更点、ページ表示、リンク、必要な動作を確認してmainへcommit・pushする。GitHub Pagesが同じURLへ反映する。
6. 新版のタグとGitHub Releaseを作り、`downloads/`の新版ZIP3本を添付する。

```sh
python3 tools/build_site.py
git add .
git commit -m "Update teaching materials to 2026-v2"
git push
gh release create 2026-v2 downloads/*-2026-v2.zip --title "2026-v2" --notes-file RELEASE_NOTES.md
```

`RELEASE_NOTES.md` は公開する更新説明を別途作成してください。リンク先は原則として相対パスを使用します。

## 構成

- `lectures/`：講義PDF
- `assignments/`：課題PDF
- `materials/`：配付用Cサンプル・入力データ
- `downloads/`：版番号付き配付ZIP
- `course-guide.txt`：授業全般の説明

教員用解答・採点データ・参考書抜粋PDFは収録していません。体験型教材は公開対象に含めません。各資料の出典表記は資料内を参照してください。
