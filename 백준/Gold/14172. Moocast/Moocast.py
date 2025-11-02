import sys
input = sys.stdin.readline

n = int(input().rstrip())
cows = [tuple(map(int, input().rstrip().split())) for _ in range(n)]

adj = [[] for _ in range(n)]
for i in range(n):
    xi, yi, pi = cows[i]
    p2 = pi * pi
    for j in range(n):
        if i == j:
            continue
        xj, yj, _ = cows[j]
        if (xi - xj) ** 2 + (yi - yj) ** 2 <= p2:
            adj[i].append(j)

best = 0
for s in range(n):
    visited = [False] * n
    stack = [s]
    visited[s] = True
    cnt = 1
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                cnt += 1
                stack.append(v)
    if cnt > best:
        best = cnt

print(best)