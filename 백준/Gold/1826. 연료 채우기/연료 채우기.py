import heapq
import sys
input = sys.stdin.readline

n = int(input())
stations = [list(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

stations.sort(key=lambda x:(x[0], -x[1]))

i = 0
ans = 0
out = False
pq = list()

while p < l:
    while i < n and p >= stations[i][0]:
        heapq.heappush(pq, -stations[i][1])
        i += 1

    if not pq:
        out = True
        break

    p -= heapq.heappop(pq)
    ans += 1

print(-1 if out else ans)