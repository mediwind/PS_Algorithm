from sys import maxsize

import heapq as hq


def dijkstra(x, dy, graph):
    Q = list()
    dy[x] = 0
    hq.heappush(Q, (0, x))
    
    while Q:
        cost, node = hq.heappop(Q)
        if dy[node] < cost:
            continue
        
        for next_node in graph[node]:
            if dy[next_node] > cost + 1:
                dy[next_node] = cost + 1
                hq.heappush(Q, (cost + 1, next_node))

    
def solution(n, roads, sources, destination):
    answer = list()
    graph = [list() for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    
    dy = [maxsize for _ in range(n + 1)]
    dijkstra(destination, dy, graph)
    # print(dy)
    for i in sources:
        res = dy[i]
        if dy[i] == maxsize:
            res = -1
        answer.append(res)
    
    return answer