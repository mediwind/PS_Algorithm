def dfs(cur):
    if cur in ch:
        return
    ch.add(cur)

    res[cur] = 1
    for adj in graph[cur]:
        dfs(adj)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ch = set()
res = [0] * (N + 1)

if not graph[1]:
    res[1] = 1

for second in graph[1]:
    dfs(second)
print(*res[1:], sep="")