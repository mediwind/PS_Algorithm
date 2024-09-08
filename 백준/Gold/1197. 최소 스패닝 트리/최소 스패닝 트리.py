import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x]) # 경로 압축
    return parent[x]


def union(a, b):
    pa, pb = find(a), find(b)
    
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


v ,e = map(int, input().split())
parent = list(range(v + 1))
graph = list()
for _ in range(e):
    a, b, c = list(map(int, input().split()))
    graph.append([a, b, c])

graph.sort(key = lambda x: x[2])

ans = 0
for s, e, w in graph:
    if find(s) == find(e):
        continue
    
    union(s, e)
    ans += w

print(ans)