import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

# B[k]: 子供 k が食した美味しさ最大値の -1 倍
# -1 倍: bisect 起因
B = [0]*N

for a in A:
    k = bisect.bisect_right(B, -a)
    if k == N:
        print(-1)
    else:
        print(k+1)
        B[k] = -a
