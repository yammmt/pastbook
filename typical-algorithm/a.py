import bisect

N, K = list(map(int, input().split()))
# already sorted
A = list(map(int, input().split()))

ok = bisect.bisect_left(A, K)

if ok == N:
    print(-1)
else:
    print(ok)
