import sys
input = sys.stdin.readline
import heapq as hq


def dijkstra(x):
    dy = [float('inf') for _ in range(n + 1)]
    Q = list()
    hq.heappush(Q, (0, x))
    dy[x] = 0
    
    while Q:
        dist, node = hq.heappop(Q)
        if dy[node] < dist:
            continue
        
        for nnode, ndist in graph[node]:
            ndist += dist
            if dy[nnode] > ndist:
                dy[nnode] = ndist
                hq.heappush(Q, (ndist, nnode))
    
    return dy


n, r1, r2 = map(int, input().split())
graph = [list() for _ in range(n + 1)]
connected = list()
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    connected.append((a, b))

route1 = dijkstra(r1)
route2 = dijkstra(r2)
ans = float('inf')
for a, b in connected:
    ans = min(ans, route1[a] + route2[b])
    ans = min(ans, route1[b] + route2[a])

if r1 == r2:
    print(0)
else:
    print(ans)