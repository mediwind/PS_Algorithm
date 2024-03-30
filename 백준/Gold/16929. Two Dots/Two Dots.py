def DFS(x, y, dist):
    global ans, sx, sy
    
    if ch[x][y]:
        if x == sx and y == sy and dist >= 4:
#             print('sx:', sx, 'sy:', sy)
#             print('x:', x, 'y:', y)
#             print('board[sx][sy], board[x][y]:', board[sx][sy], board[x][y])
            ans = True
        return
    
    ch[x][y] = 1
    
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        
        if 0 <= xx < n and 0 <= yy < m:
            if board[xx][yy] == board[x][y]:
                DFS(xx, yy, dist + 1)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ans = False
for i in range(n):
    for j in range(m):
        ch = [[0 for _ in range(m)] for _ in range(n)]
        sx, sy = i, j
        DFS(sx, sy, 0)

if ans:
    print('Yes')
else:
    print('No')