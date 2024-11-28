import sys
input = sys.stdin.readline


def DFS(x, y, time, eat):
    global ans, t
    
    if time == t:
        ans = max(ans, eat)
        return
    
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if xx < 0 or xx >= r or yy < 0 or yy >= c:
            continue
        if board[xx][yy] == '.':
            DFS(xx, yy, time + 1, eat)
        elif board[xx][yy] == 'S':
            board[xx][yy] = '.'
            DFS(xx, yy, time + 1, eat + 1)
            board[xx][yy] = 'S'
    

    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c, t = map(int, input().split())
board = [list(input()) for _ in range(r)]

ans = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'G':
            board[i][j] = '.'
            DFS(i, j, 0, 0)

print(ans)