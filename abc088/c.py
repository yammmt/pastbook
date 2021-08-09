c = []
for _ in range(0, 3):
    cc = list(map(int, input().split()))
    c.append(cc)

b3 = [c[0][0], c[0][1], c[0][2]]
a3 = [0, c[1][1] - b3[1], c[2][1] - b3[1]]
yes = True

for i in range(0, 3):
    for j in range(0, 3):
        if a3[i] + b3[j] != c[i][j]:
            yes = False
            break

if yes:
    print("Yes")
else:
    print("No")
