from collections import deque

import sys
input = sys.stdin.readline


def BFS(p):
    Q = deque()
    Q.append(p)
    visit.add(p)
    distances[p] = 0
    
    while Q:
        ice = Q.popleft()
        for next_ice in graph[ice]:
            if next_ice not in visit:
                Q.append(next_ice)
                visit.add(next_ice)
                distances[next_ice] = distances[ice] + 1


n, s, p = map(int, input().split())

graph = [list() for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distances = [float('inf') for _ in range(n + 1)]
visit = set()
BFS(p)

res = sorted(distances[1:s + 1])
print(n - res[0] - res[1] - 1)