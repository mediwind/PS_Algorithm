import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def DFS(node, depth):
    global order
    order += 1
    order_list[node] = order
    depth_list[node] = depth
    
    for next_node in graph[node]:
        if depth_list[next_node] == -1:
            depth_list[next_node] = depth + 1
            DFS(next_node, depth + 1)


n, m, r = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = list(map(lambda x: sorted(x, reverse=True), graph))

order_list = [0 for _ in range(n + 1)]
depth_list = [-1 for _ in range(n + 1)]
order = 0
DFS(r, 0)

ans = 0
for i in range(1, n + 1):
    if order_list[i]:
        ans += (order_list[i] * depth_list[i])
print(ans)