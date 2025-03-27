import heapq as hq
import sys
input = sys.stdin.readline


def dijkstra(start, detour, flag):
    dy = [float("inf") for _ in range(n + 1)]
    
    Q = list()
    hq.heappush(Q, (0, start))
    dy[start] = 0
    
    while Q:
        cost, node = hq.heappop(Q)
        
        if dy[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            
            if next_node == detour and flag != True:
                continue
                
            next_cost = next_cost + cost
            if next_cost < dy[next_node]:
                hq.heappush(Q, (next_cost, next_node))
                dy[next_node] = next_cost
    
    return dy
    

n, m = map(int, input().rstrip().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
x, y, z = map(int, input().rstrip().split())

detour1 = dijkstra(x, y, True)
detour2 = dijkstra(y, z, True)

if detour1[y] == float("inf") or detour2[z] == float("inf"):
    ans1 = -1
else:
    ans1 = detour1[y] + detour2[z]

no_detour = dijkstra(x, y, False)
ans2 = no_detour[z] if no_detour[z] != float("inf") else -1

print(ans1, ans2)