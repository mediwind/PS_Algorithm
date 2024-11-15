from collections import deque


def BFS(x, y):
    global num
    Q = deque()
    Q.append((x, y))
    board[x][y] = num
    ch[x][y] = 1
    
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            
            if xx < 0  or xx >= n or yy < 0 or yy >= m:
                continue
            
            if not ch[xx][yy] and board[xx][yy] == 'X':
                board[xx][yy] = num
                ch[x][y] = 1
                Q.append((xx, yy))


def BFS2(num):
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    Q = deque()
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == num:
                Q.append((i, j))
                dist[i][j] = 0
    
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            
            if dist[xx][yy] == -1 and board[xx][yy] == '.':
                dist[xx][yy] = dist[x][y] + 1
                Q.append((xx, yy))
            if board[xx][yy] != '.' and board[xx][yy] != num:
                return dist[x][y]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ch = [[0 for _ in range(m)] for _ in range(n)]
num = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'X' and not ch[i][j]:
            BFS(i, j)
            num += 1

ans = float('inf')
for i in range(1, num + 1):
    res = BFS2(i)
    if res != None:
        ans = min(ans, res)

print(ans)