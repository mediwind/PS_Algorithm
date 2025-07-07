import heapq as hq
import sys
input = sys.stdin.readline

board = [[0 for _ in range(501)] for _ in range(501)]

N = int(input().rstrip())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] = max(board[i][j], 1)

M = int(input().rstrip())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] = max(board[i][j], 2)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dp = [[float('inf') for _ in range(501)] for _ in range(501)]
dp[0][0] = 0

Q = list()
hq.heappush(Q, (dp[0][0], 0, 0))
while Q:
    cost, x, y = hq.heappop(Q)
    
    if x == 500 and y == 500:
        break
    
    if dp[x][y] < cost:
        continue
    
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        
        if xx < 0 or xx >= 501 or yy < 0 or yy >= 501:
            continue
        
        if board[xx][yy] == 2:
            continue
        
        new_cost = cost + board[xx][yy]
        if new_cost < dp[xx][yy]:
            dp[xx][yy] = new_cost
            hq.heappush(Q, (new_cost, xx, yy))

if dp[500][500] != float('inf'):
    print(dp[500][500])
else:
    print(-1)