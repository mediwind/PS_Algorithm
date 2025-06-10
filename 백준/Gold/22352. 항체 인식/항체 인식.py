from collections import deque
import sys
input = sys.stdin.readline


def change_color(x, y, color1, color2):
    Q = deque()
    Q.append((x, y))
    board_from[i][j] = color2
    
    while Q:
        x, y = Q.popleft()
        
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            
            if xx < 0 or xx >= N or yy < 0 or yy >= M:
                continue
            
            if board_from[xx][yy] == color1:
                board_from[xx][yy] = color2
                Q.append((xx, yy))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().rstrip().split())
board_from = [list(map(int, input().rstrip().split())) for _ in range(N)]
board_to = [list(map(int, input().rstrip().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if board_from[i][j] != board_to[i][j]:
            cnt += 1
            change_color(i, j, board_from[i][j], board_to[i][j])

if board_from != board_to:
    print("NO")
else:
    if cnt <= 1:
        print("YES")
    else:
        print("NO")