import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    pa, pb = parent[a], parent[b]
    
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


N, M = map(int, input().split())
parent = list(range(N + 1))
graph = [list(map(int, input().split())) for _ in range(M)]
graph.sort(key = lambda x: (x[2], x[3]))

path = list()
cost = 0
cnt = 0
for x, y, z, w in graph:
    if find(x) == find(y):
        continue
    
    union(x, y)
    path.append(z)
    cost += w
    cnt += 1

if cnt != N - 1:
    print(-1)
else:
    path.sort()
    print(''.join(map(str, path)), cost)