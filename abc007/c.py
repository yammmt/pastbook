from collections import deque

r, c = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
crc = []
for i in range(r):
    s = input()
    crc.append(s)

sx -= 1
sy -= 1
gx -= 1
gy -= 1

dist = []
for i in range(r):
    dist.append([-1] * c)

q = deque()
q.append([sy, sx])
dist[sy][sx] = 0

while len(q) > 0:
    i, j = q.popleft()
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if not (0 <= i2 < r and 0 <= j2 < c):
            continue
        if crc[i][j] == '#':
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            q.append([i2, j2])

print(dist[gy][gx])
