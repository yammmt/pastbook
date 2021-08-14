H, W = map(int, input().split())

A = []
for _ in range(H):
    a = input()
    A.append(a)

MOD = 10**9+7

dp = []
for _ in range(H):
    cur = [0]*W
    dp.append(cur)
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            continue

        if j-1 >= 0:
            dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
        if i-1 >= 0:
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD

print(dp[H-1][W-1])
