from collections import deque
import sys
input = sys.stdin.readline


def BFS(s, e):
    ch = [[-1 for _ in range(W)] for _ in range(H)]
    
    sx, sy = locations[s]

    Q = deque()
    Q.append((sx, sy))
    ch[sx][sy] = 0

    while Q:
        x, y = Q.popleft()
        if board[x][y] == e:
            return ch[x][y]

        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]

            if xx < 0 or xx >= H or yy < 0 or  yy >= W:
                continue

            if ch[xx][yy] == -1 and board[xx][yy] != 'X':
                Q.append((xx, yy))
                ch[xx][yy] = ch[x][y] + 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

H, W, N = map(int, input().split())
board = [list(input()) for _ in range(H)]

locations = dict()

for i in range(H):
    for j in range(W):
        tmp = board[i][j]
        if tmp == 'S':
            board[i][j] = 0
            locations[0] = (i, j)
        elif tmp.isdigit():
            board[i][j] = int(tmp)
            locations[int(tmp)] = (i, j)

ans = 0
for s in range(N):
    ans += BFS(s, s + 1)

print(ans)