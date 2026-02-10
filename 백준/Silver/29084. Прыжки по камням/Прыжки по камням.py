from collections import deque
import sys

n, k = map(int, input().split())
stones = set(map(int, input().split())) if k > 0 else set()

allowed = stones | {n}

INF = 10**18
dist = [INF] * (n + 1)
prev = [-1] * (n + 1)
prev_jump = [-1] * (n + 1)

q = deque()
dist[0] = 0
q.append(0)

while q:
    x = q.popleft()
    for jump in (1, 2):
        nx = x + jump
        if nx > n:
            continue
        if nx != n and nx not in allowed:
            continue
        if dist[nx] == INF:
            dist[nx] = dist[x] + 1
            prev[nx] = x
            prev_jump[nx] = jump
            q.append(nx)

if dist[n] == INF:
    print(-1)
    sys.exit(0)

path = []
cur = n
while cur != 0:
    path.append(str(prev_jump[cur]))
    cur = prev[cur]
path.reverse()

print(dist[n])
print("".join(path))