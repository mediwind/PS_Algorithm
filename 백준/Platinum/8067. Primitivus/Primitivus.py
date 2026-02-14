import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

parent = [i for i in range(1001)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX


n = int(input().strip())

indegree = [0] * 1001
outdegree = [0] * 1001

active_nodes = set()

for _ in range(n):
    u, v = map(int, input().strip().split())
    outdegree[u] += 1
    indegree[v] += 1

    active_nodes.add(u)
    active_nodes.add(v)
    union(u, v)

components = {}
for node in active_nodes:
    root = find(node)
    if root not in components:
        components[root] = []
    components[root].append(node)

total_paths = 0

for root in components:
    nodes = components[root]

    start_points = 0
    for node in nodes:
        if outdegree[node] > indegree[node]:
            start_points += (outdegree[node] - indegree[node])

    if start_points > 0:
        total_paths += start_points
    else:
        total_paths += 1

print(n + total_paths)