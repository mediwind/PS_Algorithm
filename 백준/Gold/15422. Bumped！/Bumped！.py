import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, F, S, T = map(int, input().strip().split())

graph = [[] for _ in range(2 * N)]

for _ in range(M):
    u, v, c = map(int, input().strip().split())

    graph[u].append((c, v))
    graph[v].append((c, u))

    graph[u + N].append((c, v + N))
    graph[v + N].append((c, u + N))

for _ in range(F):
    u, v = map(int, input().split())
    graph[u].append((0, v + N))

dist = [INF] * (2 * N)
dist[S] = 0
pq = []

heapq.heappush(pq, (0, S))

while pq:
    current_cost, u = heapq.heappop(pq)

    if dist[u] < current_cost:
        continue

    for weight, v in graph[u]:
        next_cost = current_cost + weight
        if next_cost < dist[v]:
            dist[v] = next_cost
            heapq.heappush(pq, (next_cost, v))

ans = min(dist[T], dist[T + N])
print(ans)