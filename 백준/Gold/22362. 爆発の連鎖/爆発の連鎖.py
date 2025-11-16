from collections import deque
import sys
input = sys.stdin.readline

while True:
    W, H, N, D, B = map(int, input().split())
    if (W, H, N, D, B) == (0, 0, 0, 0, 0):
        break
    pts = [tuple(map(int, input().split())) for _ in range(N)]
    adj = [[] for _ in range(N)]
    for i in range(N):
        xi, yi = pts[i]
        for j in range(i + 1, N):
            xj, yj = pts[j]
            if xi == xj and abs(yi - yj) <= D:
                adj[i].append(j); adj[j].append(i)
            elif yi == yj and abs(xi - xj) <= D:
                adj[i].append(j); adj[j].append(i)

    start = B - 1
    vis = [False] * N
    q = deque([start])
    vis[start] = True
    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)
    print(cnt)