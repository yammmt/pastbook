# ポイントの最大値が小さいので愚直に線形探索しても間に合う

N = int(input())

X = []
for i in range(N):
    X.append([])

for i in range(N):
    a, b = list(map(int, input().split()))
    X[a-1].append(b)

cnt = [0]*101
ans = 0
for d in range(N):
    for b in X[d]:
        cnt[b] += 1
    for b in range(100, 0, -1):
        if cnt[b] > 0:
            ans += b
            cnt[b] -= 1
            break
    print(ans)
