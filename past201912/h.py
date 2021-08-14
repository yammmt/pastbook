n = int(input())
cn = list(map(int, input().split()))
q = int(input())

ans = 0
set_sell = 0
all_sell = 0
set_min = 1_000_000_001
all_min = 1_000_000_001
for i in range(0, n):
    if i % 2 == 0:
        set_min = min(set_min, cn[i])
    all_min = min(all_min, cn[i])

for _ in range(0, q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        # 単品販売
        x = s[1] - 1
        a = s[2]
        if x % 2 == 0:
            card_x = cn[x] - all_sell - set_sell
        else:
            card_x = cn[x] - all_sell

        if card_x >= a:
            cn[x] -= a
            ans += a
            if i % 2 == 0:
                set_min = min(set_min, cn[x])
            else:
                all_min = min(all_min, cn[x])
    elif s[0] == 2:
        # 番号が奇数 (1-indexed) であるカードを a 枚ずつ販売
        a = s[1]
        if set_min >= set_sell + all_sell + a:
            set_sell += a
    else:
        # 全種類販売
        a = s[1]
        if min(set_min - set_sell - all_sell, all_min - all_sell) >= a:
            all_sell += a

ans += set_sell * ((n + 1) // 2)
ans += all_sell * n

print(ans)
