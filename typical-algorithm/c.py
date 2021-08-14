N = int(input())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ALL = 1 << N

# cost[n][i]: 訪れた都市の集合が n で最後にいる都市が i であるときのコスト最小値
cost = []
for n in range(ALL):
    cost.append([10**100]*N)
cost[0][0] = 0


def has_bit(n, i):
    return (n & (1 << i) > 0)


for n in range(ALL):
    # i -> j
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            cost[n | (1 << j)][j] = min(cost[n | (1 << j)][j], cost[n][i] + A[i][j])

print(cost[ALL-1][0])
