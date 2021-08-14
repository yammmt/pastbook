A, B, C = map(int, input().split())

D = A * (A + 1) // 2
E = B * (B + 1) // 2
F = C * (C + 1) // 2

ans = (D * E * F) % 998_244_353

print(ans)
