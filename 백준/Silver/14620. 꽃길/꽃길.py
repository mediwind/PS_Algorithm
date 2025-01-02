def checking(x, y):
    for d in range(5):
        xx = x + dx[d]
        yy = y + dy[d]
        if ch[xx][yy]:
            return False
    return True


def DFS(L, cost):
    global ans
    
    if L == 3:
        ans = min(ans, cost)
        return
        
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            if not ch[x][y] and checking(x, y):
                
                for d in range(5):
                    xx = x + dx[d]
                    yy = y + dy[d]
                    ch[xx][yy] = True
                    
                res = 0
                for d in range(5):
                    res += board[x + dx[d]][y + dy[d]]
                
                DFS(L + 1, cost + res)
                
                for d in range(5):
                    xx = x + dx[d]
                    yy = y + dy[d]
                    ch[xx][yy] = False


dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[False for _ in range(n)] for _ in range(n)]

ans = float("inf")
DFS(0, 0)
print(ans)