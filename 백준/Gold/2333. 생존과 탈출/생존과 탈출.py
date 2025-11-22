import sys

def max_survive_now(dp_arr, curT):
        best_hp = max(v for v in dp_arr if v >= 0) if any(v >= 0 for v in dp_arr) else -1
        if best_hp < 0:
            return curT
        return curT + best_hp

D, G = map(int, input().split())

boxes = []
for _ in range(G):
    T, F, H = map(int, input().split())
    boxes.append((T, F, H))
boxes.sort()
groups = []
i = 0
while i < G:
    t = boxes[i][0]
    grp = []
    while i < G and boxes[i][0] == t:
        grp.append(boxes[i][1:])  # (F,H)
        i += 1
    groups.append((t, grp))

NEG = -10**9
dp = [NEG] * (D + 1)
dp[0] = 10
prevT = 0

for (t, grp) in groups:
    dt = t - prevT
    dec_dp = [NEG] * (D + 1)
    for h in range(D + 1):
        if dp[h] >= 0:
            if dp[h] >= dt:
                dec_dp[h] = dp[h] - dt
    if not any(x >= 0 for x in dec_dp):
        best_hp = max((v for v in dp if v >= 0), default=-1)
        if best_hp < 0:
            print(prevT)
        else:
            print(prevT + best_hp)
        sys.exit(0)
    dp = dec_dp

    for (F, H) in grp:
        nxt = [NEG] * (D + 1)
        for h in range(D + 1):
            if dp[h] < 0:
                continue
            base_hp = dp[h]
            if base_hp > nxt[h]:
                nxt[h] = base_hp
            eat_hp = base_hp + F
            if eat_hp > nxt[h]:
                nxt[h] = eat_hp
            nh = min(D, h + H)
            if base_hp > nxt[nh]:
                nxt[nh] = base_hp
        dp = nxt
    if dp[D] >= 0:
        print(t)
        sys.exit(0)
    prevT = t

best_hp = max((v for v in dp if v >= 0), default=-1)
if best_hp < 0:
    print(prevT)
else:
    print(prevT + best_hp)