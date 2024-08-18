from collections import deque


def BFS(x, y):
    Q = deque()
    Q.append((x, y))
    power[x][y] = 16
    
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx >= h or yy < 0 or yy >= w:
                continue
            if board[xx][yy] == "redstone_dust" and power[xx][yy] < power[x][y] - 1:
                power[xx][yy] = power[x][y] - 1
                Q.append((xx, yy))
            elif board[xx][yy] == "redstone_lamp" and power[xx][yy] < power[x][y] - 1:
                power[xx][yy] = power[x][y] - 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

w, h = map(int, input().split())
n = int(input())

board = [["O" for _ in range(w)] for _ in range(h)]
for _ in range(n):
    spot, y, x = input().split()
    y, x = int(y), int(x)
    board[x][y] = spot

Q = deque()
power = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if board[i][j] == "redstone_block":
            BFS(i, j)

answer = "success"
for i in range(h):
    for j in range(w):
        if board[i][j] == "redstone_lamp" and power[i][j] <= 0:
            answer = "failed"
print(answer)