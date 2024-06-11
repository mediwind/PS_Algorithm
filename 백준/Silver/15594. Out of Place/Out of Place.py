N = int(input())
curr_line = [int(input()) for _ in range(N)]
right_line = sorted(curr_line)

# curr_line
# right_line

cnt = 0
for c, r in zip(curr_line, right_line):
    if c != r:
        cnt += 1

print(max(0, cnt - 1))