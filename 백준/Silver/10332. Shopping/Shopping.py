# 10332 
import sys
input = sys.stdin.readline

N, m = map(int, input().rstrip().split())

if not m:
    print(N + 1)
    sys.exit(0)

intervals = [tuple(map(int, input().rstrip().split())) for _ in range(m)]
intervals.sort(key = lambda x: x[0])
total = 0

cur_lt, cur_rt = intervals[0]
for lt, rt in intervals[1:]:
    if lt <= cur_rt:
        cur_rt = max(rt, cur_rt)
    else:
        total += cur_rt - cur_lt
        cur_lt, cur_rt = lt, rt

total += cur_rt - cur_lt
ans = (N + 1) + 2 * total
print(ans)