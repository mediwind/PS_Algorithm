import sys
input = sys.stdin.readline
sys.setrecursionlimit(600000)


def DFS(node, paths):
    global ans
    if len(graph[node]) == 1 and ch[graph[node][0]]:
        ans += paths
        return
    
    for next_node in graph[node]:
        if not ch[next_node]:
            ch[next_node] = 1
            DFS(next_node, paths + 1)


n = int(input())
graph = [list() for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ch = [0 for _ in range(n + 1)]
ans = 0
ch[1] = 1
DFS(1, 0)
if ans % 2:
    print("Yes")
else:
    print("No")