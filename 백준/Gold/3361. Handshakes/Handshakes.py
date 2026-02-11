import sys
# input = sys.stdin.readline().strip()

cnt_l = 0
total_handshakes = 0
last_t = 0
max_t = 0

s = input()
for char in reversed(s):
    if char == 'L':
        cnt_l += 1
    else:
        total_handshakes += cnt_l

        if cnt_l > 0:
            curr_t = max(cnt_l, last_t + 1)
            max_t = max(max_t, curr_t)
            last_t = curr_t
        else:
            last_t = 0

print(f"{max_t} {total_handshakes}")