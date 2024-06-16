n, m = map(int, input().split())

graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    color = [5, 1, 2, 3, 4]
    for node in graph[i]:
        color[answer[node]] = 5
    answer[i] = min(color)

print(''.join(map(str, answer[1:])))