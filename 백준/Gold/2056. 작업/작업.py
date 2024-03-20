from collections import deque

n = int(input())
graph = [list() for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
dy = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    order = list(map(int, input().split()))
    time[i] = order[0]
    if order[1]:
        for j in range(2, len(order)):
            degree[i] += 1
            graph[order[j]].append(i)

Q = deque()
for i in range(1, n + 1):
    if not degree[i]:
        Q.append(i)
        dy[i] = time[i]

while Q:
    x = Q.popleft()
    order.append(x)
    for i in graph[x]:
        degree[i] -= 1
        dy[i] = max(dy[i], dy[x] + time[i])
        if not degree[i]:
            Q.append(i)

print(max(dy[1:]))