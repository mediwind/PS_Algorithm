from collections import deque


def BFS():
    Q = deque()
    time[0][0] = 0
    Q.append((0, 0, 0))
    while Q:
        x, y, passed = Q.popleft()
        for d in range(3):
            xx = x + dx[d]
            yy = y + dy[d]
            if d == 2:
                xx %= 2
            
            if passed > y:
                continue
            if xx < 0 or xx >= 2 or yy < 0:
                continue
            if yy >= n:
                return True
            if not board[xx][yy]:
                continue

            if time[xx][yy] == -1:
                time[xx][yy] = time[x][y] + 1
                Q.append((xx, yy, passed + 1))
    
    return False


n, k = map(int, input().split())

dx = [0, 0, 1]
dy = [1, -1, k]

board = [list(map(int, input())) for _ in range(2)]
time = [[-1 for _ in range(n)] for _ in range(2)]

res = BFS()
if res:
    print(1)
else:
    print(0)