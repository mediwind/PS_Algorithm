import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


n, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    j = i + 1 if i < n else 1
    adj[i].append(j)
    adj[j].append(i)

for _ in range(k):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for v in range(1, n + 1):
    adj[v].sort(key=lambda x: (x - v) % n)

visited = set()
faces = []

for u in range(1, n + 1):
    for v in adj[u]:
        if (u, v) in visited:
            continue

        cur_u, cur_v = u, v
        cnt = 0

        while True:
            visited.add((cur_u, cur_v))
            cnt += 1

            neighbors = adj[cur_v]
            idx = neighbors.index(cur_u)
            next_v = neighbors[(idx + 1) % len(neighbors)]

            cur_u, cur_v = cur_v, next_v

            if (cur_u, cur_v) == (u, v):
                break

        faces.append(cnt)

faces.sort()

print(faces[-2])