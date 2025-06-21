from collections import deque
import sys
input = sys.stdin.readline


def drill(mid):
    cnt = 0
    ch = [[0 for _ in range(M)] for _ in range(N)]
    
    for sx, sy in start_position:
        if board[sx][sy] <= mid and not ch[sx][sy]:
            Q = deque()
            Q.append((sx, sy))
            cnt += 1
            ch[sx][sy] = 1
            
            while Q:
                x, y = Q.popleft()
                
                for d in range(4):
                    xx = x + dx[d]
                    yy = y + dy[d]
                    
                    if xx < 0 or xx >= N or yy < 0 or yy >= M:
                        continue
                        
                    if board[xx][yy] > mid:
                        continue
                    
                    if ch[xx][yy]:
                        continue
                    
                    Q.append((xx, yy))
                    cnt += 1
                    ch[xx][yy] = 1
    
    return cnt


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

start_position = list()
for col in range(M):
    start_position.append((0, col))
for row in range(1, N):
    start_position.append((row, 0))
    start_position.append((row, M - 1))

ans = float('inf')
lt, rt = 1, max(map(max, board))
while lt <= rt:
    mid = (lt + rt) // 2
    res = drill(mid)
    if res >= K:
        ans = min(ans, mid)
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)