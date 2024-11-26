import heapq as hq
import sys
input = sys.stdin.readline


def dijkstra(x):
    Q = list()
    dist[x] = 0
    hq.heappush(Q, (0, x))
    prev = [-1] * (n + 1)  # 이전 노드를 기록하는 리스트
    
    while Q:
        cost, node = hq.heappop(Q)
        if dist[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                prev[next_node] = node  # 이전 노드를 기록
                hq.heappush(Q, (new_cost, next_node))
    
    return prev


def find_paths(prev):
    paths = list()
    for node in range(2, n + 1):
        if prev[node] != -1:
            paths.append((prev[node], node))
    return paths


n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [float('inf') for _ in range(n + 1)]
prev = dijkstra(1)
paths = find_paths(prev)
print(len(paths))
for a, b in paths:
    print(a, b)