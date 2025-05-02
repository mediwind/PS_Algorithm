import sys
input = sys.stdin.readline

MAX_COORD = 10**6 + 1

max_r = [-1 for _ in range(MAX_COORD)]
min_l = [MAX_COORD for _ in range(MAX_COORD)]
exact_intervals = set()

N = int(input())

for _ in range(N):
    li, ri = map(int, input().split())
    max_r[li] = max(max_r[li], ri)
    min_l[ri] = min(min_l[ri], li)
    exact_intervals.add((li, ri))

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())

    if (l, r) in exact_intervals:
        print(1)
        continue

    cond1_met = (l < MAX_COORD and max_r[l] != -1 and max_r[l] >= r)
    cond2_met = (r < MAX_COORD and min_l[r] != MAX_COORD and min_l[r] <= l)

    if cond1_met and cond2_met:
        print(2)
    else:
        print(-1)