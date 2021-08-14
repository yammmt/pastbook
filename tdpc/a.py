import copy

N = int(input())
pn = list(map(int, input().split()))

dp_size = sum(pn) + 1
dp = [False]*dp_size
dp[0] = True
for i in range(N):
    cur = copy.deepcopy(dp)
    for j in range(dp_size):
        if j - pn[i] >= 0 and dp[j-pn[i]]:
            cur[j] = True
    dp = cur

print(dp.count(True))
