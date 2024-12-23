from collections import deque


def BFS(x):
    Q = deque()
    Q.append((x, 0))
    visited[x] = 0
    while Q:
        pos, dist = Q.popleft()
        if pos == m:
            return dist
        for option in [pos - 1, pos + 1, pos - a, pos - b, pos + a, pos + b, pos * a, pos * b]:
            if option in visited:
                continue
            if 0 <= option <= 100000:
                Q.append((option, dist + 1))
                visited[option] = dist + 1
    

a, b, n, m = map(int, input().split())
visited = dict()
print(BFS(n))