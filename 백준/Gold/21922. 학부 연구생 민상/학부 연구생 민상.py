from collections import deque
import sys
input = sys.stdin.readline


def way_check(sx, sy):
    ch[sx][sy] = 1
    for d in range(4):
        Q = deque()
        Q.append((sx, sy, d))
        while Q:
            x, y, d = Q.popleft()
                
            xx = x + drct[d][0]
            yy = y + drct[d][1]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                break
            if board[xx][yy] == 9:
                break
            
            ch[xx][yy] = 1
            if board[xx][yy] == 1 and d in [1, 3]:
                break
            if board[xx][yy] == 2 and d in [0, 2]:
                break
            
            if board[xx][yy] == 3:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                else:
                    d = 2
            elif board[xx][yy] == 4:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                else:
                    d = 0
            
            Q.append((xx, yy, d))


drct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

aircon = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 9]

ch = [[0 for _ in range(m)] for _ in range(n)]
for sx, sy in aircon:
    way_check(sx, sy)

ans = sum(map(sum, ch))
print(ans)