import sys
input = sys.stdin.readline


def DFS(cur, cnt):

    if cnt > 7:
        return 1

    if dy[cur][cnt] != -1:
        return dy[cur][cnt]

    dy[cur][cnt] = 0
    for nxt in graph[cur]:
        dy[cur][cnt] = (dy[cur][cnt] + DFS(nxt, cnt + 1)) % MOD

    return dy[cur][cnt]


ans = 0
MOD = 1e9 + 7
N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
dy = [[-1 for _ in range(8)] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    ans = (ans + DFS(i, 1)) % MOD

print(f'{ans:.0f}')