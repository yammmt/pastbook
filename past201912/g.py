N = int(input())
A = []
for i in range(N-1):
    # 0 から i まではダミーで埋める
    lst = list(map(int, input().split()))
    A.append([0]*(i+1) + lst)

ALL = 1 << N
happy = [0]*ALL


# 集合 n に要素 i が含まれれば True
def has_bit(n, i):
    return (n & (1 << i) > 0)


# 幸福度は繰り返し使うので前計算しておく
for n in range(ALL):
    for i in range(N):
        for j in range(i+1, N):
            if has_bit(n, i) and has_bit(n, j):
                happy[n] += A[i][j]

ans = -10**100

for n1 in range(ALL):
    for n2 in range(ALL):
        if n1 & n2 > 0:
            continue
        n3 = ALL-1 - (n1 | n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans)
