def dfs(graph, start, cut, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                if not cut[neighbor] and not visited[neighbor]:
                    stack.append(neighbor)


p, c, n = map(int, input().split())

graph = [[] for _ in range(p + 1)]

for _ in range(c):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cut = [False] * (p + 1)
for _ in range(n):
    x = int(input())
    for neighbor in graph[x]:
        cut[neighbor] = True

visited = [False] * (p + 1)
dfs(graph, 1, cut, visited)

ans = p
for i in range(1, p + 1):
    if visited[i]:
        ans -= 1

print(ans)