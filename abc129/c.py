N, M = map(int, input().split())

ok = [True]*(N+1)
for i in range(M):
    a = int(input())
    ok[a] = False

MOD = 10**9+7

dp = [0]*(N+1)
dp[0] = 1

for i in range(1, N+1):
    if not ok[i]:
        continue

    if i == 1:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[N])
