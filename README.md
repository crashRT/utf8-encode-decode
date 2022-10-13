# utf8-encode-decode
文字列をUTF8の16進数で表示したり戻したりするスクリプト

## エンコード

`encode.py` の `encodeToUTF8` は
文字列を受け取ってUTF8の16進数に変換して返す関数

例：
```
hogehogeにゃーん
-> 68 6F 67 65 68 6F 67 65 E3 81 AB E3 82 83 E3 83 BC E3 82 93
```

## デコード
`decode.py` の `decodeFromUTF8` は 
上の`encodeToUTF8`で変換された16進数を受け取って元の文字列に戻す関数

例：
```
E3 81 AB E3 82 83 E3 83 BC E3 82 93 → にゃーん
```
