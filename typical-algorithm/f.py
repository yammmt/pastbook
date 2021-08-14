# 最小全域木 (プリム法)

import heapq

N, M = map(int, input().split())

edges = []
for _ in range(N):
    edges.append([])

for _ in range(M):
    u, v, c = map(int, input().split())
    edges[u].append((c, v))
    edges[v].append((c, u))

marked = [False]*N
marked_cnt = 0
dist = [10**100]*N
Q = []
# (建設コスト, 頂点)
heapq.heappush(Q, (0, 0))
dist[0] = 0
ans = 0
while marked_cnt < N:
    cur = heapq.heappop(Q)
    if marked[cur[1]]:
        continue

    ans += cur[0]
    marked[cur[1]] = True
    marked_cnt += 1
    if marked_cnt == N:
        break
    for i in range(len(edges[cur[1]])):
        next_cost = edges[cur[1]][i][0]
        next_idx = edges[cur[1]][i][1]
        if not marked[next_idx] and next_cost < dist[next_idx]:
            dist[next_idx] = next_cost
            heapq.heappush(Q, (next_cost, next_idx))

print(ans)
