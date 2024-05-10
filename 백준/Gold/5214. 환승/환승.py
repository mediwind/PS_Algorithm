from collections import defaultdict

import heapq
import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
INF = float('inf')

graph = defaultdict(list)
cost = [INF] * (N + M)

for m in range(M):
    stations = list(map(int, input().split()))
    for n in stations:
        n -= 1
        graph[n].append(N + m)
        graph[N + m].append(n)

heap = [(0, 0)]
cost[0] = 0

while heap:
    cur_cost, cur = heapq.heappop(heap)
    if cost[cur] < cur_cost:
        continue

    for next_node in graph[cur]:
        distance = 0 if next_node >= N else 1
        if cost[next_node] > cost[cur] + distance:
            cost[next_node] = cost[cur] + distance
            heapq.heappush(heap, (cost[next_node], next_node))

if cost[N - 1] != INF:
    print(cost[N - 1] + 1)
else:
    print(-1)