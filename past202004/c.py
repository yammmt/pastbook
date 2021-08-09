n = int(input())
s = []
for _ in range(0, n):
    ss = list(input())
    s.append(ss)

for i in range(n-2, -1, -1):
    for j in range(1, 2*n-1):
        if (s[i][j] == "#" and
                (s[i+1][j-1] == "X" or s[i+1][j] == "X" or
                    s[i+1][j+1] == "X")):
            s[i][j] = "X"

for i in range(0, n):
    print(''.join(s[i]))
