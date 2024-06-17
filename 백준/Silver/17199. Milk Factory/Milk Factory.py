n = int(input())
graph = [list() for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = 0
for i in range(1, n + 1):
    if answer and not graph[i]:
        answer = -1
        break
    if not graph[i]:
        answer = i

print(answer)