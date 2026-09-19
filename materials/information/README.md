# 情報理論：課題1・2の配付ファイル

課題PDFに従って、サンプルプログラムと入力データを使用してください。

- `kraft_sample.c`：語頭符号生成の穴埋め用サンプル
- `huffman_sample.c`：ハフマン符号の穴埋め用サンプル
- `alphabet_prob.txt`、`n_array_huffman.txt`：確率分布などの入力データ
- `not_inst_enc.txt`：課題で指定された符号化の入力データ
- `lz78-internal.txt`：LZ78の入力データ

サンプル中の `// ???` は各自で実装する箇所です。未完成の状態では正しい実行結果は得られません。

コンパイル例（C11）:

```sh
gcc -std=c11 kraft_sample.c -o kraft.out
gcc -std=c11 huffman_sample.c -lm -o huffman.out
```

プログラムとレポートは、指定された授業システムに電子データとして提出してください。
