import heapq as hq
import sys
input = sys.stdin.readline

T, n = map(int, input().split())
Q = list()
for _ in range(n):
    a, b, c = map(int, input().split())
    hq.heappush(Q, [-c, a, b])

for _ in range(T):
    pr, ids, time = hq.heappop(Q)
    print(ids)
    pr += 1
    time -= 1
    if time >= 1:
        hq.heappush(Q, [pr, ids, time])