n, ll = list(map(int, input().split()))
xn = list(map(int, input().split()))
t3 = list(map(int, input().split()))

# ハードル由来のロスタイムを一律 0 で初期化してやる
h = [0]*(ll+1)
for x in xn:
    h[x] = t3[2]

cost = [10**100] * (ll+1)
cost[0] = 0

for i in range(1, ll+1):
    # 1
    cost[i] = min(cost[i], cost[i-1]+t3[0])
    # 2
    if i >= 2:
        cost[i] = min(cost[i], cost[i-2]+t3[0]+t3[1])
    # 3
    if i >= 4:
        cost[i] = min(cost[i], cost[i-4]+t3[0]+3*t3[1])
    cost[i] += h[i]

# ジャンプ中に超えた場合も考える
ans = cost[ll]
for i in [ll-3, ll-2, ll-1]:
    if i >= 0:
        ans = min(ans, cost[i] + t3[0]//2 + t3[1]*(2*(ll-i)-1)//2)

print(ans)
