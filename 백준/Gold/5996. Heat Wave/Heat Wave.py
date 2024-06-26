import heapq as hq
import sys
input = sys.stdin.readline


def dijkstra(x):
    Q = list()
    hq.heappush(Q, (0, x))
    dy[x] = 0
    
    while Q:
        cost, node = hq.heappop(Q)
        if dy[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            next_cost += cost
            if dy[next_node] >= next_cost:
                hq.heappush(Q, (next_cost, next_node))
                dy[next_node] = next_cost


t, c, s, e = map(int, input().split())
graph = [list() for _ in range(t + 1)]
for _ in range(c):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))


dy = [float('inf') for _ in range(t + 1)]
dijkstra(s)
print(dy[e])