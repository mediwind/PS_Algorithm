import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def DFS(node):
    for next_node in graph[node]:
        if ch[next_node] == -1:
            ch[next_node] = ch[node] + 1
            DFS(next_node)


N, M, R = map(int, input().split())

graph = [list() for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

ch = [-1 for _ in range(N + 1)]
ch[R] = 0

DFS(R)
for c in ch[1:]:
    print(c)