a = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    a.append(row)

m = [[False, False, False], [False, False, False], [False, False, False]]

n = int(input())
for _ in range(0, n):
    b = int(input())
    for i in range(0, 3):
        for j in range(0, 3):
            if a[i][j] == b:
                m[i][j] = True

yes = False

# 行
for i in range(0, 3):
    if m[i][0] and m[i][1] and m[i][2]:
        yes = True

# 列
for i in range(0, 3):
    if m[0][i] and m[1][i] and m[2][i]:
        yes = True

# 斜め
if (m[0][0] and m[1][1] and m[2][2]) or (m[0][2] and m[1][1] and m[2][0]):
    yes = True

if yes:
    print("Yes")
else:
    print("No")
