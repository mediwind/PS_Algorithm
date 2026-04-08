import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(u):
    visited[u] = True

    dp0 = 0
    dp1 = energy[u]

    for v in graph[u]:
        if not visited[v]:
            c0, c1 = dfs(v)

            dp0 += max(c0, c1)
            dp1 += c0

    return dp0, dp1


n, m = map(int, input().split())

energy = [int(input()) for _ in range(n)]
protons = [int(input()) for _ in range(m)]

energy_set = set(energy)

graph = [[] for _ in range(n)]

energy_index = {energy[i]: i for i in range(n)}

for i in range(n):
    for p in protons:
        target = energy[i] + p
        if target in energy_set:
            j = energy_index[target]
            graph[i].append(j)
            graph[j].append(i)

visited = [False] * n

answer = 0

for i in range(n):
    if not visited[i]:
        dp0, dp1 = dfs(i)
        answer += max(dp0, dp1)

print(answer)