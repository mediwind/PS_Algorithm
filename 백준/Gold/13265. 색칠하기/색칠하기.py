from collections import deque
import sys
input = sys.stdin.readline


def check():
    for node in range(1, N + 1):
        for next_node in graph[node]:
            if color[node] == color[next_node]:
                return "impossible"
    
    return "possible"


T = int(input().rstrip())
for _ in range(T):
    N, M = map(int, input().rstrip().split())
    graph = [list() for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().rstrip().split())
        graph[x].append(y)
        graph[y].append(x)

    color = [-1 for _ in range(N + 1)]

    for i in range(1, N + 1):
        if color[i] == -1:
            Q = deque()
            Q.append(i)
            color[i] = 1
            while Q:
                node = Q.popleft()
                for next_node in graph[node]:
                    if color[next_node] == -1:
                        color[next_node] = 0 if color[node] else 1
                        Q.append(next_node)
    
    print(check())