from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx, sy, num):
    ch[sx][sy] = num
    Q = deque()
    Q.append((sx, sy))
    
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            
            xx %= n
            yy %= m
            
            if not ch[xx][yy] and not board[xx][yy]:
                ch[xx][yy] = num
                Q.append((xx, yy))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for i in range(n):
    for j in range(m):
        if not ch[i][j] and not board[i][j]:
            cnt += 1
            BFS(i, j, cnt)

# for c in ch:
#     print(c)
# print()
print(cnt)