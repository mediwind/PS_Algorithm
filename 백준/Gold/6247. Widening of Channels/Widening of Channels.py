from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
adj = [[] for _ in range(n + 1)]
edges = list()
for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    edges.append((u, v, w))
k = int(input())

for u, v, w in edges:
    if w >= k:
        adj[u].append(v)
        adj[v].append(u)

visited = [False for _ in range(n + 1)]
components = 0
for i in range(1, n + 1):
    if not visited[i]:
        components += 1
        q = deque([i])
        visited[i] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

print(max(0, components - 1))