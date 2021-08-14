import sys
sys.setrecursionlimit(1_000_000)

n = int(input())
hn = list(map(int, input().split()))

cost = [0] * n
done = [False] * n


def rec(i):
    if done[i]:
        return cost[i]

    if i == 0:
        cost[i] = 0
    elif i == 1:
        cost[i] = rec(0) + abs(hn[0]-hn[1])
    else:
        cost[i] = min(rec(i-1)+abs(hn[i-1]-hn[i]), rec(i-2)+abs(hn[i-2]-hn[i]))
    done[i] = True
    return cost[i]


print(rec(n - 1))
