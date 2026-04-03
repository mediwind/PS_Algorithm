from collections import deque
import sys
input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def mark_vision(x, y, d, t):
    while True:
        x += dx[d]
        y += dy[d]

        if not in_range(x, y):
            break

        if grid[x][y] == '.':
            blocked[t][x][y] = True
        else:
            break


n, m = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())

sx -= 1
sy -= 1
ex -= 1
ey -= 1

grid = []
ghosts = []

for i in range(n):
    row = list(input().strip())
    grid.append(row)
    for j, c in enumerate(row):
        if c not in ('#', '.'):
            ghosts.append((i, j, int(c)))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

blocked = [[[False] * m for _ in range(n)] for _ in range(4)]

for t in range(4):
    for gx, gy, d in ghosts:
        nd = (d + t) % 4
        mark_vision(gx, gy, nd, t)

visited = [[[False] * m for _ in range(n)] for _ in range(4)]

queue = deque()
queue.append((sx, sy, 0))
visited[0][sx][sy] = True

answer = 0

while queue:
    x, y, time = queue.popleft()

    if x == ex and y == ey:
        answer = time
        break

    next_time = time + 1
    state = next_time % 4

    if not blocked[state][x][y] and not visited[state][x][y]:
        visited[state][x][y] = True
        queue.append((x, y, next_time))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue

        if grid[nx][ny] != '.':
            continue

        if blocked[state][nx][ny]:
            continue

        if visited[state][nx][ny]:
            continue

        visited[state][nx][ny] = True
        queue.append((nx, ny, next_time))

if answer:
    print(answer)
else:
    print("GG")