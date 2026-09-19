#!/usr/bin/env python3
"""Build the static landing page and immutable, deterministic release archives."""
from pathlib import Path
import hashlib
import html
import io
import json
import re
import zipfile

B = Path(__file__).resolve().parents[1]
release = json.loads((B / 'release.json').read_text())
version = release['version']
assert re.fullmatch(r'[A-Za-z0-9.-]+', version)
date = release['date']
repo = 'https://github.com/' + release['repository']
downloads = B / 'downloads'
downloads.mkdir(exist_ok=True)

def archive(name, paths):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in sorted(paths):
            info = zipfile.ZipInfo(f'ict-experiment-2-{version}/' + p.relative_to(B).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())
        info = zipfile.ZipInfo(f'ict-experiment-2-{version}/VERSION.txt', (2026, 1, 1, 0, 0, 0))
        z.writestr(info, f'{version}\n{date}\n{repo}/releases/tag/{version}\n')
    p = downloads / f'{name}-{version}.zip'
    data = buffer.getvalue()
    if p.exists() and p.read_bytes() != data:
        raise SystemExit(f'{p.name} already exists with different contents. Increment release.json version/tag; do not overwrite a published release.')
    p.write_bytes(data)
    return p

def files(folder):
    return [p for p in (B / folder).rglob('*') if p.is_file() and p.name != '.DS_Store']

program_info = archive('information-programs', files('materials/information'))
program_code = archive('coding-data', files('materials/coding'))
all_files = files('lectures') + files('assignments') + files('materials') + files('interactive') + [B / 'course-guide.txt']
bundle = archive('ict-experiment-2', all_files)

info_tools = [
    ('語頭符号', 'prefix_code_trainer.html', '符号語長から木を組み立てる'),
    ('ハフマン符号', 'huffman_trainer.html', '確率の小さい節点を順に結ぶ'),
    ('最小ヒープ', 'minheap_trainer.html', '追加・取り出しと木の変化を見る'),
    ('算術符号', 'arithmetic_coding.html', '記号列に応じた区間の変化を追う'),
    ('LZ78', 'LZ78.html', '辞書の成長と符号化を観察する'),
]
coding_tools = [
    ('RS符号の考え方', 'RS.html', '実数上の評価点と補間で仕組みを学ぶ'),
    ('ポーラ符号', 'polar.html', '消失通信路の分極とSC復号を見る'),
    ('APM-LDPC', 'APM-LDPC.html', 'サイクルと合成関数の関係を調べる'),
]

def tool_cards(items, section):
    return ''.join(f'<a class="tool" href="interactive/{section}/{filename}"><span>{title}</span><small>{desc}</small><b aria-hidden="true">↗</b></a>' for title, filename, desc in items)

def shell(title, main):
    return f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="情報通信実験第2の情報理論・符号理論の講義資料、課題、配付プログラム、体験型教材。">
<meta name="theme-color" content="#173d34"><title>{title} | 情報通信実験第2</title><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#main">本文へ移動</a><header class="top"><a class="brand" href="./">情報通信実験第2</a><nav aria-label="主なメニュー"><a href="./#materials">配付資料</a><a href="./#interactive">体験型教材</a><a href="updates.html">更新履歴</a></nav></header>
<main id="main">{main}</main><footer><span>情報通信実験第2 · 情報理論・符号理論<br>Kenta Kasai</span><span><a href="{repo}">GitHub</a> · <a href="{repo}/releases">過去の配付版</a><br>更新日 {date}</span></footer></body></html>'''

main = f'''<section class="hero"><div><p class="eyebrow">ICT.E218 / COURSE MATERIALS</p><h1>情報を圧縮する。<br>誤りから、取り戻す。</h1><p class="intro">情報通信実験第2の情報理論・符号理論の教材です。<br>講義で学び、プログラムで確かめ、図を動かして理解を深めましょう。</p><div class="actions"><a class="button primary" href="downloads/{bundle.name}" download>教材一式をダウンロード <span>↓</span></a><a class="text-link" href="#materials">課題ごとに選ぶ →</a></div><p class="version">配付版 <strong>{version}</strong><span>更新 {date}</span><a href="updates.html">変更内容を見る</a></p></div><aside class="hero-note"><span class="note-label">このページの使い方</span><ol><li><b>課題を読む</b><span>PDFで内容と入出力を確認</span></li><li><b>ファイルを取得する</b><span>ZIPをダウンロードして展開</span></li><li><b>実装して、提出する</b><span>レポート・プログラムは授業システムへ</span></li></ol></aside></section>
<section id="materials"><div class="section-head"><div><p class="eyebrow">01 / MATERIALS</p><h2>講義と実験の資料</h2></div><a class="text-link" href="course-guide.txt">授業全般の説明 ↗</a></div><div class="materials-grid">
<article class="material-card"><span class="pill">課題 1・2</span><h3>情報理論</h3><p>語頭符号・ハフマン符号・算術符号・LZ78</p><div class="links"><a href="assignments/information.pdf">課題1・2を読む <span>PDF ↗</span></a><a href="lectures/information-01.pdf">講義資料 前半 <span>PDF ↗</span></a><a href="lectures/information-02.pdf">講義資料 後半 <span>PDF ↗</span></a></div><a class="button secondary" href="downloads/{program_info.name}" download>プログラム・入力データ <span>ZIP ↓</span></a><small>Cサンプルは穴埋め用です。未実装の箇所を完成させてください。</small></article>
<article class="material-card"><span class="pill">課題 3・4</span><h3>符号理論</h3><p>線形符号・有限体・リード・ソロモン符号</p><div class="links"><a href="assignments/coding.pdf">課題3・4を読む <span>PDF ↗</span></a><a href="lectures/coding.pdf">講義資料 前半＋後半 <span>PDF ↗</span></a></div><a class="button secondary" href="downloads/{program_code.name}" download>入力データ・入出力例 <span>ZIP ↓</span></a><small>プログラムは課題PDFの仕様に従って作成してください。</small></article></div>
<div class="submission"><strong>提出は授業システムから</strong><p>プログラムとレポートは、指定されたシステムに電子データとして提出してください。締切・ファイル形式は授業内およびシステム上の案内に従ってください。</p></div></section>
<section id="interactive"><div class="section-head"><div><p class="eyebrow">02 / INTERACTIVE</p><h2>動かして理解する</h2></div><p>リンクを開くと、ブラウザで操作できます。</p></div><h3 class="group-title">情報理論</h3><div class="tool-grid">{tool_cards(info_tools,'information')}</div><h3 class="group-title">符号理論</h3><div class="tool-grid">{tool_cards(coding_tools,'coding')}</div><p class="muted">RS教材は、符号の仕組みを説明する実数版です。有限体上の実装は講義資料・課題PDFを参照してください。一部の教材は数式表示にインターネット接続を使用します。</p></section>
<section class="updates-note"><div><p class="eyebrow">03 / UPDATES</p><h2>更新しても、入口は同じ。</h2><p>このページには現在の配付版を掲載します。各版のZIPは保存されるので、以前の教材も確認できます。授業で版が指定された場合は、その版を使ってください。</p></div><a class="button secondary" href="updates.html">更新履歴と過去の版 →</a></section>'''
(B / 'index.html').write_text(shell('教材ページ', main))

blocks = []
for line in (B / 'CHANGELOG.md').read_text().splitlines():
    if line.startswith('## '): blocks.append('<h2>' + html.escape(line[3:]) + '</h2>')
    elif line.startswith('- '): blocks.append('<p class="change-item">' + html.escape(line[2:]) + '</p>')
    elif line and not line.startswith('#'): blocks.append('<p>' + html.escape(line) + '</p>')
updates = '<section class="history"><p class="eyebrow">CHANGELOG</p><h1>更新履歴</h1><p>教材の変更内容と配付版を確認できます。旧版のZIPはGitHub Releasesから取得できます。</p><a class="button secondary" href="' + repo + '/releases">過去の配付版を開く ↗</a><article>' + ''.join(blocks) + '</article></section>'
(B / 'updates.html').write_text(shell('更新履歴', updates))
manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [bundle, program_info, program_code]}
(downloads / f'SHA256SUMS-{version}.txt').write_text(''.join(f'{sha}  {name}\n' for name, sha in manifest.items()))
print(json.dumps({'version':version,'archives':manifest},ensure_ascii=False,indent=2))
