from collections import deque


def BFS(hx, hy, hz):
    Q = deque()
    Q.append((hx, hy, hz))
    while Q:
        x, y, z = Q.popleft()
        if x == Ex and y == Ey:
            return ch[x][y][z]
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            
            if xx < 0 or xx >= N or yy < 0 or yy >= M:
                continue
            
            if board[xx][yy] == 1 and z == 0:
                ch[xx][yy][1] = ch[x][y][0] + 1
                Q.append((xx, yy, 1))
            elif board[xx][yy] == 0 and ch[xx][yy][z] == -1:
                ch[xx][yy][z] = ch[x][y][z] + 1
                Q.append((xx, yy, z))
    
    return -1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
Hx, Hy = map(lambda x: int(x) - 1, input().split())
Ex, Ey = map(lambda x: int(x) - 1, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
ch = [[[-1, -1] for _ in range(M)] for _ in range(N)]
ch[Hx][Hy][0] = 0
print(BFS(Hx, Hy, 0))