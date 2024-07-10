from collections import deque


def path_check(a, b):
    cnt = 0
    for i in range(k):
        if a[i] != b[i]:
            cnt += 1
        if cnt >= 2:
            return False
    return True


n, k = map(int, input().split())
bits = [0] + [input() for _ in range(n)]
graph = [list() for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if path_check(bits[i], bits[j]):
            graph[i].append(j)
            graph[j].append(i)
a, b = map(int, input().split())
# graph

distance = [-1 for _ in range(n + 1)]
previous = [-1 for _ in range(n + 1)]  # 경로 추적을 위한 배열
distance[a] = 0
Q = deque([a])

while Q:
    node = Q.popleft()
    if node == b:
        break
    for next_node in graph[node]:
        if distance[next_node] == -1:
            distance[next_node] = distance[node] + 1
            previous[next_node] = node  # 이전 노드를 기록
            Q.append(next_node)

# previous
# 경로 추적
path = []
current = b
while current != -1:
    path.append(current)
    current = previous[current]
path.reverse()

# distance
if distance[b] == -1:
    print(-1)
else:
    print(*path)