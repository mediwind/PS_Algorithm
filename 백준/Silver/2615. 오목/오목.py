import sys


def BFS(x, y):
    start = board[x][y]
    
    for d in range(4):
        cnt = 1
        xx = x + dx[d]
        yy = y + dy[d]
        
        while 0 <= xx < 19 and 0 <= yy < 19 and board[xx][yy] == start:
            cnt += 1
            
            if cnt == 5:
                if 0 <= x - dx[d] < 19 and 0 <= y - dy[d] < 19 and board[x - dx[d]][y - dy[d]] == start:
                    break
                if 0 <= xx + dx[d] < 19 and 0 <= yy + dy[d] < 19 and board[xx + dx[d]][yy + dy[d]] == start:
                    break
                
                return True
            
            xx += dx[d]
            yy += dy[d]

    return False


dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

board = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if board[i][j]:
            res = BFS(i, j)
            if res:
                print(board[i][j])
                print(i + 1, j + 1)
                sys.exit(0)

print(0)