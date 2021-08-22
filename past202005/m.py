# TSP + bitDP
# PyPy で出す

from collections import deque

N, M = list(map(int, input().split()))

# 無向グラフ
edges = []
for _ in range(N):
    edges.append([])
for _ in range(M):
    u, v = list(map(int, input().split()))
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

S = int(input())
S -= 1
K = int(input())
T = list(map(int, input().split()))
for i in range(K):
    T[i] -= 1

T.append(S)

# Dist[k][l]: 頂点 T[k] から T[l] までの移動コスト
Dist = []
INF = 10**100
for t1 in T:
    dist = [INF]*N
    que = deque()
    que.append(t1)
    dist[t1] = 0
    while len(que) > 0:
        while len(que) > 0:
            i = que.popleft()
            for j in edges[i]:
                if dist[j] == INF:
                    dist[j] = dist[i] + 1
                    que.append(j)
    res = []
    for t2 in T:
        res.append(dist[t2])
    Dist.append(res)

# TSP
# cost[n][i]: T の中で訪れた頂点の集合が n で現在地が i であるときのコスト最小値
ALL = 1 << K
cost = []
for _ in range(ALL):
    cost.append([INF]*K)

# S -> T[i] を初期状態
for i in range(K):
    # T.append(S) 行より始点は K 番目 (0-indexed)
    cost[1 << i][i] = Dist[K][i]


def has_bit(n, i):
    return (n & (1 << i) > 0)


for n in range(ALL):
    for i in range(K):
        for j in range(K):
            if has_bit(n, j) or i == j:
                continue
            cost[n | (1 << j)][j] = min(cost[n | (1 << j)][j], cost[n][i] + Dist[i][j])

print(min(cost[ALL-1]))
