from collections import deque


def BFS():
    Q = deque()
    Q.append((0, 0))
    ch[0][0] = 0
    
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if 0 <= xx < n and 0 <= yy < m:
                if ch[xx][yy] == -1 and board[xx][yy] != 1:
                    Q.append((xx, yy))
                    ch[xx][yy] = ch[x][y] + 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            sword = [i, j]

ch = [[-1 for _ in range(m)] for _ in range(n)]
BFS()

if ch[n-1][m-1] == -1:
    res1 = float('inf')
else:
    res1 = ch[n-1][m-1]

sx, sy = sword
if ch[sx][sy] != -1:
    res2 = (n-1) - sx + (m-1) - sy
else:
    res2 = float('inf')
res2 += ch[sx][sy]

ans = min(res1, res2)
if ans == float('inf') or ans > t:
    print("Fail")
else:
    print(ans)