import sys
sys.setrecursionlimit(10**8)


def dfs(x, y, color):
    global result
    result = max(1, result)
    visited[x][y] = color
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] == 'X':
            if visited[nx][ny] == -1:
                result = max(2, result)
                dfs(nx, ny, (color + 1) % 2)
            elif visited[nx][ny] == color:
                print(3)
                exit(0)


N = int(input())
board = [list(input()) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
result = 0
directions = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]

for x in range(N):
    for y in range(N):
        if board[x][y] == 'X' and visited[x][y] == -1:
            dfs(x, y, 0)
print(result)