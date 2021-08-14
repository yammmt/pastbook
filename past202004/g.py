from collections import deque
from string import ascii_lowercase

Q = int(input())
que = deque()

for _ in range(Q):
    values = input().split()
    if values[0] == '1':
        c = values[1]
        x = int(values[2])
        que.append([c, x])
    else:
        d = int(values[1])
        cnt = {}
        for c in ascii_lowercase:
            cnt[c] = 0
        while d > 0 and len(que) > 0:
            c, x = que[0]
            if d >= x:
                # 全部取る
                d -= x
                cnt[c] += x
                que.popleft()
            else:
                cnt[c] += d
                que[0][1] -= d
                d = 0
        ans = 0
        for c in ascii_lowercase:
            ans += cnt[c] ** 2
        print(ans)
