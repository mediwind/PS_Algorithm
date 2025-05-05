from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

Q = deque()
ch = [-1 for _ in range(n + 1)]

Q.append((r, 0))
ch[r] = 0
while Q:
    x, depth = Q.popleft()
    for neighbor in graph[x]:
        if ch[neighbor] == -1:
            ch[neighbor] = depth + 1
            Q.append((neighbor, depth + 1))

for d in ch[1:]:
    print(d)