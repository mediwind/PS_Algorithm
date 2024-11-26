import heapq as hq
import sys
input = sys.stdin.readline


def dijkstra(x):
    Q = list()
    dist[x] = 0
    hq.heappush(Q, (0, x))
    prev = [-1 for _ in range(n + 1)]
    
    while Q:
        cost, node = hq.heappop(Q)
        if dist[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            next_cost += cost
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                prev[next_node] = node
                hq.heappush(Q, (next_cost, next_node))
    
    return prev


n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [float('inf') for _ in range(n + 1)]
prev = dijkstra(1)
paths = list()
for node in range(2, n + 1):
    if prev[node] != -1:
        paths.append((prev[node], node))

print(len(paths))
for a, b in paths:
    print(a, b)