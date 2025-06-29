from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx, sy, direction):
    Q = deque()
    Q.append((sx, sy, direction))
    
    cnt = 0
    while Q:
        x, y, direction = Q.popleft()
        
        xx = x + dx[direction]
        yy = y + dy[direction]
        
        if xx < 0 or xx >= N or yy < 0 or yy >= M:
            return cnt + 1
        
        if ch[xx][yy][direction]:
            print(direction_map[direction])
            print("Voyager")
            sys.exit(0)
        
        if board[xx][yy] == 'C':
            return cnt + 1
        
        ch[xx][yy][direction] = 1
        if board[xx][yy] == '.':
            pass
        elif board[xx][yy] == '/':
            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 3
            else:
                direction = 2
        else:
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            else:
                direction = 0
        
        Q.append((xx, yy, direction))
        cnt += 1
            

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction_map = {0: 'U', 1: 'R', 2: 'D', 3: 'L'}

N, M = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(N)]

ans = [0 for _ in range(4)]
sx, sy = map(int, input().rstrip().split())
for i in range(4):
    ch = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]
    res = BFS(sx - 1, sy - 1, i)
    ans[i] = res

maxi = max(ans)
for i in range(4):
    if ans[i] == maxi:
        print(direction_map[i])
        break
print(maxi)