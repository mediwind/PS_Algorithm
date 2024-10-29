from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx, sy):
    Q = deque()
    Q.append((sx, sy))
    ch[sx][sy] = 1
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx >= w or yy < 0 or yy >= h:
                continue
            if not ch[xx][yy] and board[xx][yy] == '#':
                Q.append((xx, yy))
                ch[xx][yy] = 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(w)]
    ch = [[0 for _ in range(h)] for _ in range(w)]

    cnt = 0
    for i in range(w):
        for j in range(h):
            if not ch[i][j] and board[i][j] == '#':
                cnt += 1
                BFS(i, j)

    print(cnt)