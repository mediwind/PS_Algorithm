from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
degree = [0 for _ in range(n + 1)]
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1
# graph
# degree

Q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        Q.append((i, 1))
# Q

answer = [0 for _ in range(n + 1)]
while Q:
    x, semester = Q.popleft()
    answer[x] = semester
    for node in graph[x]:
        if degree[node] > 0:
            degree[node] -= 1
            if degree[node] == 0:
                Q.append((node, semester + 1))

print(*answer[1:])