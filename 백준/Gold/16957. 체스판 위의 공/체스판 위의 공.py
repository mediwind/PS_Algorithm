import sys
input = sys.stdin.readline


def find(x, y):
    if destination[x][y]:
        return destination[x][y]
    
    min_val = board[x][y]
    min_pos = (x, y)
    
    for d in range(8):
        xx = x + dx[d]
        yy = y + dy[d]
        
        if xx < 0 or xx >= R or yy < 0 or yy >= C:
            continue
        
        if board[xx][yy] >= min_val:
            continue
        
        min_val = board[xx][yy]
        min_pos = (xx, yy)
        
    if min_pos == (x, y):
        destination[x][y] = (x, y)
    else:
        destination[x][y] = find(min_pos[0], min_pos[1])
    
    return destination[x][y]


R, C = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(R)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

destination = [[0 for _ in range(C)] for _ in range(R)]

ans = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        x, y = find(i, j)
        ans[x][y] += 1

for row in ans:
    print(*row)