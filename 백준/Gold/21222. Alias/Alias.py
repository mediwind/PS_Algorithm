import heapq as hq
import sys
input = sys.stdin.readline


def dijkstra(s, e):
    Q = list()
    hq.heappush(Q, (0, s))
    found = False
    
    while Q:
        cost, node = hq.heappop(Q)
        
        if node == e:
            print(cost)
            found = True
            return
        
        if dy[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            next_cost += cost
            if next_cost < dy[next_node]:
                dy[next_node] = next_cost
                hq.heappush(Q, (next_cost, next_node))
    
    print('Roger')
                

N, M = map(int, input().strip().split())
name_to_id = dict()
id_counter = 0
graph = [list() for _ in range(N)]
for _ in range(M):
    x, y, c = input().strip().split(); c = int(c)
    
    if x not in name_to_id:
        name_to_id[x] = id_counter
        id_counter += 1
    if y not in name_to_id:
        name_to_id[y] = id_counter
        id_counter += 1
    
    a, b = name_to_id[x], name_to_id[y]
    graph[a].append((b, c))

Q = int(input())
for _ in range(Q):
    dy = [float('inf') for _ in range(N)]
    start, end = input().strip().split()
    s, e = name_to_id[start], name_to_id[end]
    dy[s] = 0
    dijkstra(s, e)