def DFS(x, y, visited):
    global cnt
    
    if x == 4 and y == 4 and visited == no_block:
        cnt += 1
        return
    
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        if xx < 0 or xx > 4 or yy < 0 or yy > 4:
            continue
        if board[xx][yy] == -1:
            continue
        if ch[xx][yy] == -1:
            ch[xx][yy] = ch[x][y] + 1
            DFS(xx, yy, visited + 1)
            ch[xx][yy] = -1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [[0 for _ in range(5)] for _ in range(5)]
ch = [[-1 for _ in range(5)] for _ in range(5)]
k = int(input())
no_block = 25 - k
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = -1

ch[0][0] = 0
cnt = 0
DFS(0, 0, 1)
print(cnt)