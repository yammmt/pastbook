n, m, q = map(int, input().split())

graph = []
for _ in range(0, n):
    graph.append([])

for _ in range(0, m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

c = list(map(int, input().split()))

for _ in range(0, q):
    query = list(map(int, input().split()))

    x = query[1]
    x -= 1
    print(c[x])
    if query[0] == 1:
        for i in graph[x]:
            c[i] = c[x]
    else:
        y = query[2]
        c[x] = y
