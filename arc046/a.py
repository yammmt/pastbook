n = int(input())

num = (n-1) % 9 + 1
digit = (n-1) // 9

ans = num
for _ in range(0, digit):
    ans *= 10
    ans += num

print(ans)
