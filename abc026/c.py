import sys
sys.setrecursionlimit(1_000_000)

N = int(input())
child = []
for _ in range(N):
    child.append([])
for i in range(1, N):
    b = int(input())
    child[b-1].append(i)


def dfs(i):
    if len(child[i]) == 0:
        return 1
    else:
        values = []
        for j in child[i]:
            values.append(dfs(j))
        return max(values) + min(values) + 1


print(dfs(0))
