from collections import deque
import sys
input = sys.stdin.readline

N, W = map(int, input().rstrip().split())

graph = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

ch = [0 for _ in range(N + 1)]
ch[1] = 1

Q = deque()
Q.append(1)
cnt = 0
while Q:
    node = Q.popleft()
    
    leaf_flag = True
    for next_node in graph[node]:
        if not ch[next_node]:
            ch[next_node] = 1
            Q.append(next_node)
            leaf_flag = False
    
    if leaf_flag:
        cnt += 1

print(W / cnt)