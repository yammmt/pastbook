# 半分全列挙

from collections import defaultdict

N, X = list(map(int, input().split()))

A = []
B = []
for i in range(N):
    w = int(input())
    if i % 2 == 0:
        A.append(w)
    else:
        B.append(w)


def has_bit(n, i):
    return (n & (1 << i) > 0)


# グループ B を全列挙して重さ合計ごとに集計
dic = defaultdict(int)
for n in range(1 << len(B)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += B[i]
    dic[s] += 1

ans = 0
for n in range(1 << len(A)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += A[i]
    ans += dic[X-s]

print(ans)
