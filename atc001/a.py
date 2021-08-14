# 再帰上限を増やす (AtCoder ではデフォルト 1,000)
import sys
sys.setrecursionlimit(1_000_000)

h, w = list(map(int, input().split()))
chw = []
for _ in range(h):
    s = input()
    chw.append(s)

for i in range(h):
    for j in range(w):
        if chw[i][j] == 's':
            si, sj = i, j
        elif chw[i][j] == 'g':
            gi, gj = i, j

visited = []
for i in range(h):
    visited.append([False] * w)


def dfs(i, j):
    visited[i][j] = True
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if not (0 <= i2 < h and 0 <= j2 < w):
            continue
        if chw[i][j] == '#':
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)


dfs(si, sj)

if visited[gi][gj]:
    print("Yes")
else:
    print("No")
