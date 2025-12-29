from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx, sy):
    global ans
    Q = deque()
    Q.append((sx, sy))
    ch[sx][sy] = 1
    
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            
            if xx < 0 or xx >= 102 or yy < 0 or yy >= 102:
                continue
            
            if ch[xx][yy]:
                continue
            
            if board[xx][yy] == 1:
                ans += 1
                continue
                
            ch[xx][yy] = 1
            Q.append((xx, yy))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

n = int(input().strip())
board = [[0 for _ in range(102)] for _ in range(102)]
ch = [[0 for _ in range(102)] for _ in range(102)]
for _ in range(n):
    x, y = map(int, input().strip().split())
    board[x][y] = 1

BFS(0, 0)

print(ans)