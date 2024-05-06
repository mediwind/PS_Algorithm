from collections import deque


def BFS(x, y):
    Q = deque()
    Q.append((x, y))
    ch[x][y] =1 
    flag = True
    
    while Q:
        x, y = Q.popleft()
        for d in range(8):
            xx = x + dx[d]
            yy = y + dy[d]
            
            if xx >= 0 and xx < n and yy >= 0 and yy < m:
                if board[xx][yy] > board[x][y]:
                    flag = False
                elif board[xx][yy] == board[x][y] and not ch[xx][yy]:
                    Q.append((xx, yy))
                    ch[xx][yy] = 1
        
    return flag


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ch = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if not ch[i][j]:
            res = BFS(i, j)
            if res:
                ans += 1
print(ans)