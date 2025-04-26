from collections import deque
import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
sx, sy = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

Q = deque([[0, sx - 1, sy - 1]])
ch = [[0 for _ in range(M)] for _ in range(N)]

dy = [0 for _ in range(10 ** 6)]

while Q:
    l, x, y = Q.popleft()
    if x < 0 or x >= N or y < 0 or y >= M:
        continue
    if ch[x][y] == 1:
        continue
    ch[x][y] = 1
    if graph[x][y] == -1:
        continue

    dy[l] += graph[x][y]
    Q.append([l + 1, x + 1, y])
    Q.append([l + 1, x - 1, y])
    Q.append([l + 1, x, y + 1])
    Q.append([l + 1, x, y - 1])

max_dy = 0
now_dy = C
for i in range(l + 1):
    now_dy += dy[i] - C
    max_dy = max(now_dy, max_dy)

print(max_dy)