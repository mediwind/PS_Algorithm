def moving(x, y):
    ch[x][y] = 0
    
    while True:
        yy = y + 1
        if yy >= W:
            break
            
        if board[x][yy] == '.':
            ch[x][yy] = ch[x][y] + 1
        else:
            break
            
        y = yy


H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

ch = [[-1 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if board[i][j] == 'c':
            moving(i, j)

for c in ch:
    print(*c)