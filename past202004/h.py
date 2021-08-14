N, M = list(map(int, input().split()))
anm = []
for _ in range(N):
    a = input()
    anm.append(a)

group = []
for _ in range(11):
    group.append([])
for i in range(N):
    for j in range(M):
        if anm[i][j] == 'S':
            n = 0
        elif anm[i][j] == 'G':
            n = 10
        else:
            n = int(anm[i][j])
        group[n].append([i, j])

cost = []
INF = 10**100
for _ in range(N):
    cost.append([INF]*M)

si, sj = group[0][0]
cost[si][sj] = 0

for n in range(1, 11):
    for i, j in group[n]:
        for i2, j2 in group[n-1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i-i2) + abs(j-j2))

gi, gj = group[10][0]
ans = cost[gi][gj]
if ans == INF:
    ans = -1
print(ans)
