import sys

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
    sys.exit(0)

board = [[0 for _ in range(C)] for _ in range(R)]

x, y, d = 0, 0, 0
for num in range(1, C * R + 1):
    if num == K:
        print(y + 1, x + 1)
        break
    board[x][y] = num
    x += dx[d]
    y += dy[d]
    
    if x < 0 or x >= R or y < 0 or y >= C or board[x][y]:
        x -= dx[d]
        y -= dy[d]
        d = (d + 1) % 4
        x += dx[d]
        y += dy[d]