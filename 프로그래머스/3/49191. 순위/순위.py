from collections import deque


def BFS(n, idx, graph):
    ch = [0 for _ in range(n + 1)]
    
    Q = deque()
    ch[idx] = 1
    distance = 0
    Q.append(idx)
    
    while Q:
        x = Q.popleft()
        for i in graph[x]:
            if not ch[i]:
                ch[i] = 1
                distance += 1
                Q.append(i)
    
    return distance


def solution(n, results):
    graph = [list() for _ in range(n + 1)]
    graph_reversed = [list() for _ in range(n + 1)]
    
    for a, b in results:
        graph[a].append(b)
        graph_reversed[b].append(a)
    
    # print(graph)
    # print(graph_reversed)
    
    rank = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        rank[i] += BFS(n, i, graph)
        rank[i] += BFS(n, i, graph_reversed)
    
    # print(rank)
    
    answer = rank[1:].count(n - 1)
    return answer