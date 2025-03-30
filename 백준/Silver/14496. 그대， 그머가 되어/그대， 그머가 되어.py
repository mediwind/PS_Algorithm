from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
n, m = map(int, input().rstrip().split())

graph = [list() for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

ch = [-1 for _ in range(n + 1)]
ch[a] = 0

Q = deque()
Q.append(a)
while Q:
    node = Q.popleft()
    for next_node in graph[node]:
        if ch[next_node] == -1:
            ch[next_node] = ch[node] + 1
            Q.append(next_node)
print(ch[b])