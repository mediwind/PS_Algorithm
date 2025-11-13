import sys
input = sys.stdin.readline

n = int(input().rstrip())
min_sum = 10**18
max_sum = -10**18
min_diff = 10**18
max_diff = -10**18

for _ in range(n):
    x, y = map(int, input().rstrip().split())
    s = x + y
    d = x - y
    if s < min_sum:
        min_sum = s
    if s > max_sum:
        max_sum = s
    if d < min_diff:
        min_diff = d
    if d > max_diff:
        max_diff = d

print(max(max_sum - min_sum, max_diff - min_diff))