import sys
sys.setrecursionlimit(10**5 * 2 + 1)
input = sys.stdin.readline


def DFS(p_node, c_node):
    global ans
    ch[c_node] = 1
    
    if colors[p_node] != colors[c_node]:
        ans += 1
    
    for next_node in graph[c_node]:
        if not ch[next_node]:
            DFS(c_node, next_node)
    

N = int(input().rstrip())
colors = list(map(int, input().rstrip().split()))
colors.insert(0, 0)
graph = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

ch = [0 for _ in range(N + 1)]
ch[0] = 1

ans = 0
DFS(0, 1)
print(ans)