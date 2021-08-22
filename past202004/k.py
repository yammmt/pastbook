# PyPy

N = int(input())
# インデックス揃えのためにダミーを入れておく
S = " " + input()
C = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))

INF = 10**100

# cost[i][j]: i 文字目まで見てそこまでの累積和が j であるときのコスト最小値
cost = []
for _ in range(N+1):
    cost.append([INF]*(N+1))
cost[0][0] = 0

for i in range(1, N+1):
    for j in range(i):
        if S[i] == "(":
            # そのまま使う
            cost[i][j+1] = min(cost[i][j+1], cost[i-1][j])
            if j > 0:
                # 反転
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j] + C[i])
        else:
            if j > 0:
                # そのまま使う
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j])
            #　反転
            cost[i][j+1] = min(cost[i][j+1], cost[i-1][j] + C[i])
        # 削除
        cost[i][j] = min(cost[i][j], cost[i-1][j] + D[i])

print(cost[N][0])
