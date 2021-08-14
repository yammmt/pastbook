N = int(input())

arr = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    arr.append([-a-b, a, b])

arr.sort()
ans = 0
for i in range(N):
    c, a, b = arr[i]
    if i % 2 == 0:
        ans += a
    else:
        ans -= b

print(ans)
