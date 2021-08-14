n = int(input())
hn = list(map(int, input().split()))

cost = [0] * n

cost[1] = cost[0] + abs(hn[0]-hn[1])
for i in range(2, n):
    cost[i] = min(cost[i-1]+abs(hn[i]-hn[i-1]), cost[i-2]+abs(hn[i]-hn[i-2]))

print(cost[n - 1])
