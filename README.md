# pastbook

[アルゴリズム実技検定 公式テキスト[エントリー〜中級編]](https://book.mynavi.jp/ec/products/detail/id=120229)

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
