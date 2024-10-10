# 要求仕様書

コマンドの使用例を以下に示す。

```
# 1〰9の数字を使った足し算 10問生成する。
$ python calc_quiz.py randint(1,9)+randint(1,9)

# 1〰9の数字を使った足し算 20問生成する。
$ python calc_quiz.py randint(1,9)+randint(1,9) --num=20

# 1〰9の数字を使った足し算 10問生成する。
# 答えの範囲は1より大きく10未満
$ python calc_quiz.py randint(1,9)+randint(1,9) --cond='1<ans<10'

# 割り算 答えに余り禁止
$ python calc_quiz.py randint(1,81)/randint(1,81) --remainder=0

# 3つの項の演算 式に括弧を含み、途中の計算では負の値を出さないようにする。
$ python calc_quiz.py randint(1,100)[+,-,*]randint(1,100)[+,-,*]randint(1,100) --cond='0<ans<800' --include='()'  --cond='0<value'
```

計算結果の出力例を以下に示す。

```
$ python calc_quiz.py randint(1,9)+randint(1,9)

# quiz
1. 2+3=
2. 4+5=
・・・
10. 1+3=

# answer
1. 2+3=5
2. 4+5=9
・・・
10. 1+3=4
```
