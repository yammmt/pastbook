# pastbook

[アルゴリズム実技検定 公式テキスト[エントリー〜中級編]](https://book.mynavi.jp/ec/products/detail/id=120229)

## Python と PyPy

(p.72) 雑には

- 再帰関数は Python
- ループの回数が多い場合には PyPy

## 忘備録

文法なんもわからん

### 配列入力を受け取る

```python
s = list(map(int, input().split()))
```

### 文字列の配列を受け取る

```python
s = list(input())
```

### 二次元配列入力を受け取る

```python
a = []
for _ in range(0, 3):
    row = list(map(int, input().split()))

    a.append(row)
```

### 二次元配列の初期化

N 行 M 列

```python
arr = [[0]*M for _ in range(N)]
```

```python
arr = []
for _ in range(N):
    arr.append([0]*M)
```

### アルファベット演算

```python
ord("x") - ord("c") # 21
chr(ord("c") + 10) # m
```

## :pray: 書籍レポジトリ

[kenkoooo/pastbook-source-code](https://github.com/kenkoooo/pastbook-source-code)
