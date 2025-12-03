import sys
input = sys.stdin.readline

num_chars, max_chars, num_bosses = map(int, input().split())
damages = [int(input().strip()) for _ in range(num_chars)]
bosses = [tuple(map(int, input().split())) for _ in range(num_bosses)]
per_char_profits = []

TIME_LIMIT = 900
DP_COLS = TIME_LIMIT + 1

for dmg in damages:
    need_time = [0]
    for hp, reward in bosses:
        t = hp // dmg
        if hp % dmg:
            t += 1
        need_time.append(t)

    dp_table = [[0] * DP_COLS for _ in range(num_bosses + 1)]

    for i in range(1, num_bosses + 1):
        req = need_time[i]
        reward = bosses[i - 1][1]
        prev_row = dp_table[i - 1]
        cur_row = dp_table[i]
        for t in range(1, DP_COLS):
            if t >= req:
                take = reward + prev_row[t - req]
                cur_row[t] = prev_row[t] if prev_row[t] > take else take
            else:
                cur_row[t] = prev_row[t]

    per_char_profits.append(dp_table[num_bosses][TIME_LIMIT])

per_char_profits.sort(reverse=True)
print(sum(per_char_profits[:max_chars]))