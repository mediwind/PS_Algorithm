def DFS(x, y):
    global ans
    
    if x == N:
        ans += 1
        return
    
    xx, yy = x, y + 1
    
    if yy == M:
        xx += 1
        yy = 0
    
    # 1. 넴모를 놓지 않는 경우
    DFS(xx, yy)
    
    # 2. 넴모를 놓는 경우 (2 x 2가 안 만들어질 때만)
    if x > 0 and y > 0:
        if board[x - 1][y] and board[x][y - 1] and board[x - 1][y - 1]:
            return
    
    board[x][y] = 1
    DFS(xx, yy)
    board[x][y] = 0


N, M = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
ans = 0

DFS(0, 0)
print(ans)