import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    pa, pb = find(a), find(b)
    
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


n, m = map(int, input().split())
graph = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(m)]
parent = list(range(n + 1))

graph.sort(key = lambda x: x[2])

total = sum(graph[i][2] for i in range(1, m + 1))
save = 0
edge_used = 0
for a, b, c in graph[1:]:
    pa, pb = find(a), find(b)
    if pa == pb:
        continue
    
    union(a, b)
    save += c
    edge_used += 1

if edge_used == n - 1:
    print(total - save)
else:
    print(-1)