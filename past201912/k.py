import sys
sys.setrecursionlimit(1_000_000)

N = int(input())
R = -1
edges = []
for i in range(N):
    edges.append([])

for i in range(N):
    p = int(input())
    if p == -1:
        R = i
    else:
        edges[p-1].append(i)

queries = []
for i in range(N):
    queries.append([])
Q = int(input())
for q in range(Q):
    a, b = map(int, input().split())
    queries[a-1].append([q, b-1])

ans = [False]*Q
# boss[i]: i が今見ている頂点の上司なら True
boss = [False]*N


def dfs(i):
    for q, b in queries[i]:
        ans[q] = boss[b]
    boss[i] = True
    for j in edges[i]:
        dfs(j)
    boss[i] = False


dfs(R)

for q in range(Q):
    if ans[q]:
        print("Yes")
    else:
        print("No")
