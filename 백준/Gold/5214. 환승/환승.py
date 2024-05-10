from collections import defaultdict

import heapq as hq
import sys
input = sys.stdin.readline


class CompareFirst:
    def __init__(self, tup):
        self.tup = tup

    def __lt__(self, other):
        return self.tup[0] < other.tup[0]

    def __eq__(self, other):
        return self.tup[0] == other.tup[0]

    def __repr__(self):
        return repr(self.tup)


def djikstra(x):
    Q = list()
    hq.heappush(Q, CompareFirst((0, x)))
    dy[x] = 0
    
    while Q:
        cost, node = hq.heappop(Q).tup
        if dy[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            next_cost += cost
            if dy[next_node] > next_cost:
                dy[next_node] = next_cost
                hq.heappush(Q, CompareFirst((next_cost, next_node)))                


n, k, m = map(int, input().split())
graph = defaultdict(list)
for i in range(1, m + 1):
    stations = list(map(int, input().split()))
    for st in stations:
        graph[st].append((str(i), 0))
        graph[str(i)].append((st, 1))

dy = dict()
for i in range(1, n + 1):
    dy[i] = float('inf')
for i in range(1, m + 1):
    dy[f'{i}'] = float('inf')
djikstra(1)
if dy[n] != float('inf'):
    print(dy[n] + 1)
else:
    print(-1)