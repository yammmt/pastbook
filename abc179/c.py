N = int(input())

ans = 0

for A in range(1, N):
    b_count = (N - 1) // A
    ans += b_count

print(ans)
