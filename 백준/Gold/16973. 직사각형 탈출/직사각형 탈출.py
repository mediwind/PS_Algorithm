from collections import deque

import sys
input = sys.stdin.readline


def possible(x, y):
    global H, W
    
    for wx, wy in walls:
        if x <= wx < x + H and y <= wy < y + W:
            return False

    return True


def BFS(sx, sy):
    Q = deque()
    Q.append((sx, sy))
    ch[sx][sy] = 0
    
    while Q:
        x, y = Q.popleft()
        if x == Fr and y == Fc:
            return ch[x][y]
        
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx > N - H or yy < 0 or yy > M - W:
                continue
            
            if board[xx][yy] or ch[xx][yy] != -1:
                continue
            
            if possible(xx, yy):
                Q.append((xx, yy))
                ch[xx][yy] = ch[x][y] + 1
    
    return -1



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

walls = list()
for i in range(N):
    for j in range(M):
        if board[i][j]:
            walls.append((i, j))

H, W, Sr, Sc, Fr, Fc = map(int, input().split())
Sr, Sc, Fr, Fc = map(lambda x: x - 1, [Sr, Sc, Fr, Fc])

ch = [[-1 for _ in range(M)] for _ in range(N)]
print(BFS(Sr, Sc))