import sys
input = sys.stdin.readline

N = int(input().strip())

segments = []
for _ in range(N):
    l, r = map(int, input().strip().split())
    segments.append((l, r))

l1, r1 = segments[0]

dp_l = abs(1 - r1) + (r1 - l1)    
dp_r = abs(1 - l1) + (r1 - l1)

prev_l, prev_r = l1, r1
for i in range(1, N):
    cur_l, cur_r = segments[i]
    width = cur_r - cur_l

    next_dp_l = min(dp_l + abs(prev_l - cur_r), 
                    dp_r + abs(prev_r - cur_r)) + 1 + width

    next_dp_r = min(dp_l + abs(prev_l - cur_l), 
                    dp_r + abs(prev_r - cur_l)) + 1 + width

    dp_l, dp_r = next_dp_l, next_dp_r
    prev_l, prev_r = cur_l, cur_r

ans = min(dp_l + abs(prev_l - N), dp_r + abs(prev_r - N))

print(ans)