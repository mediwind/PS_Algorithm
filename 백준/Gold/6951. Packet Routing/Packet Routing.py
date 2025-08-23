from collections import deque

N, W, P = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(W):
    a, b, t = map(int, input().split())
    adj[a].append((b, t))
    adj[b].append((a, t))

dist = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
for s in range(1, N + 1):
    dq = deque([s])
    dist[s][s] = 0
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[s][v] == -1:
                dist[s][v] = dist[s][u] + w
                dq.append(v)

for _ in range(P):
    u, v = map(int, input().split())
    print(dist[u][v])