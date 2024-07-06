import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def DFS(num, L):
    for node in graph[num]:
        if node not in visit:
            visit.add(node)
            level[node] = L
            DFS(node, L + 1)


n, m, r = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
graph = list(map(lambda x: sorted(x, reverse = True), graph))
# graph

visit = {r}
level = [-1 for _ in range(n + 1)]
level[r] = 0
DFS(r, 1)

for lv in level[1:]:
    print(lv)