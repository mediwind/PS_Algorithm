from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    boarder = max(map(max, rectangle)) * 2
    board = [[-1 for _ in range(boarder + 2)] for _ in range(boarder + 2)]
    
    for rec in rectangle:
        y1, x1, y2, x2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0:
                    board[i][j] = 1
    
    for bd in board:
        print(bd)
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ch = [[0 for _ in range(boarder + 2)] for _ in range(boarder + 2)]
    
    sy, sx, ey, ex = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY
    Q = deque([(sx, sy)])
    print(Q)
    while Q:
        x, y = Q.popleft()
        if x == ex and y == ey:
            answer = ch[x][y] // 2
            break
        
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            
            if board[xx][yy] == 1 and not ch[xx][yy]:
                ch[xx][yy] = ch[x][y] + 1
                Q.append((xx, yy))
    
    return answer
    
    answer = 0
    return answer