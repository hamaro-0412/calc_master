# 要求仕様書

以下のようなコマンドを実行するとランダムで計算問題が生成される。
基本はコマンド実行すると以下のような出力が得られる。  
何かオプションをつけると、pdf等で成形したファイルを出力する。 
コマンドのフォーマットはpythonのformatライクとしたい。

```
$ python math_wb.py '{:1} + {:1} = {:1}'
1 + 1 = 
1 + 2 =
3 + 4 =
  ・
  ・
  ・
```

## ファイル構成案
* 計算問題を出力するファイル 足し算・引き算・掛け算等で分ける？  
それだと、'%d + %d * %d = %d'等に対応するの難しい？

* 入力フォーマットを解析し、各クラスへ計算を頼むファイル

* 計算問題に対して回答を出力するファイル。  
こちらは現状箇条書きレベルで問題なし

* 出力された計算問題をpdfやスプレッドシート等に成形して出力するファイル。  
例えばA4用紙2列に計算問題を出力する。  
```
A4用紙のイメージ
2列にして表示したい
| 1 + 1 =  | 5 + 5 = | 
| 2 + 2 =  | 6 + 6 = |
| 3 + 3 =  | 7 + 7 = |
| 4 + 4 =  | 8 + 8 = |
```

## フォーマット例
式も答えもすべて一桁の整数
```
python math_workbook.py {1d}+{1d}={1d}
python math_workbook.py randint(1,8)+randint(1,8)={1d}
```

```
python math_workbook.py randint(1,9)+randint(1,9)={+1d} #一桁の足し算
python math_workbook.py randint(1,9)-randint(1,9)={+1d} #一桁の引き算 答えにマイナス禁止
python math_workbook.py randint(1,9)*randint(1,9)={d} #掛け算
python math_workbook.py randint(1,81)/randint(1,81)={d} #割り算　答えに余り禁止
python math_workbook.py randint(1,81)/randint(1,81)={d},R #割り算　答えに余りあり

```

式に1桁の整数を入れて、while文か何かで、一桁の整数でるまでループさせるとか。
コマンドラインでこの式書くのは冗長かも

```
f'{random.randint(1,9)}' + f'{random.randint(1,9)}' = f'{random.randint(1,9)}'
````

random関数を省いたパターン。  
上記の式よりは記載量少ない。

```
f'{randint(1,8) + randint(1,8) = randint(2,9)}'
```

足し算であれば、答えだけ記載しておけば左辺の式の候補も見つかる。

```
f'{}' + f'{}' = f'{randint(2,9)}'
```

```
f'{randint(1,8) + randint(1,8)}' < 10
```

```

