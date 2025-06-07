import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def DFS(u, parent):
    subtotal = values[u]
    
    for v in graph[u]:
        if v == parent:
            continue
            
        child_sum = DFS(v, u)
        if child_sum > 0:
            subtotal += child_sum
        
    return subtotal


N = int(input().rstrip())
graph = [list() for _ in range(N)]
for _ in range(N - 1):
    p, c = map(int, input().rstrip().split())
    graph[p].append(c)
    graph[c].append(p)

values = list(map(int, input().rstrip().split()))
ans = DFS(0, -1)
print(ans)