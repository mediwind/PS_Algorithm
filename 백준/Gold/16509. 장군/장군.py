from collections import deque

dx = [[-1, -1, -1], [-1, -1, -1], # 상좌, 상우
      [0, -1, -1], [0, 1, 1], # 우상, 우하
      [1, 1, 1,], [1, 1, 1], # 하우, 하좌
      [0, -1, -1], [0, 1, 1]] # 좌상, 좌하

dy = [[0, -1, -1], [0, 1, 1], # 상좌, 상우
      [1, 1, 1], [1, 1, 1], # 우상, 우하
      [0, 1, 1], [0, -1, -1], # 하우, 하좌
      [-1, -1, -1], [-1, -1, -1]]  # 좌상, 좌하

board = [[0 for _ in range(9)] for _ in range(10)]
ch = [[-1 for _ in range(9)] for _ in range(10)]

ex, ey = map(int, input().split())
kx, ky = map(int, input().split())

Q = deque()
Q.append((ex, ey))
ch[ex][ey] = 0
while Q:
    x, y = Q.popleft()
    
    if x == kx and y == ky:
        print(ch[kx][ky])
        break
    
    for d in range(8):
        sx = x
        sy = y
        
        x1 = sx + dx[d][0]
        y1 = sy + dy[d][0]
        
        if x1 < 0 or x1 >= 10 or y1 < 0 or y1 >= 9:
            continue
        if x1 == kx and y1 == ky:
            continue
        
        x2 = x1 + dx[d][1]
        y2 = y1 + dy[d][1]
        
        if x2 < 0 or x2 >= 10 or y2 < 0 or y2 >= 9:
            continue
        if x2 == kx and y2 == ky:
            continue
        
        x3 = x2 + dx[d][2]
        y3 = y2 + dy[d][2]
        
        if x3 < 0 or x3 >= 10 or y3 < 0 or y3 >= 9:
            continue
        
        if ch[x3][y3] == -1:
            ch[x3][y3] = ch[x][y] + 1
            Q.append((x3, y3))
else:
    print(-1)