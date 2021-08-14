import heapq

N, M = map(int, input().split())

G = []
for _ in range(N):
    G.append([])

# already 0-indexed
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))

dist = []
for _ in range(N):
    dist.append(-1)
dist[0] = 0

Q = []
# (距離, 頂点)
heapq.heappush(Q, (0, 0))

done = []
for _ in range(N):
    done.append(False)

while len(Q) > 0:
    d, i = heapq.heappop(Q)
    if done[i]:
        continue

    done[i] = True
    for (j, c) in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))

print(dist[N - 1])
