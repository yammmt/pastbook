n, q = map(int, input().split())

# graph[i][j]: i follows j
graph = []
for _ in range(0, n):
    row = []
    for _ in range(0, n):
        row.append(False)
    graph.append(row)

for _ in range(0, q):
    query = list(map(int, input().split()))
    a = query[1] - 1
    if query[0] == 1:
        b = query[2] - 1
        graph[a][b] = True
    elif query[0] == 2:
        for v in range(0, n):
            if graph[v][a]:
                graph[a][v] = True
    else:
        to_follow = []
        for v in range(0, n):
            if graph[a][v]:
                for w in range(0, n):
                    if graph[v][w] and w != a:
                        to_follow.append(w)
        for w in to_follow:
            graph[a][w] = True

for i in range(0, n):
    for j in range(0, n):
        if graph[i][j]:
            print('Y', end='')
        else:
            print('N', end='')
    print()
