def DFS(x, y, path):
    global mini, maxi
    
    path.append(board[x][y])
    ch[x][y] = 1
    
    if x == n - 1 and y == n - 1:
        temp = int(path[0])
        for i, w in enumerate(path):
            if w.isdigit():
                if path[i - 1] == '+':
                    temp += int(w)
                elif path[i - 1] == '-':
                    temp -= int(w)
                elif path[i - 1] == '*':
                    temp *= int(w)
        mini = min(mini, temp)
        maxi = max(maxi, temp)
        return
    
    for d in range(2):
        xx = x + dx[d]
        yy = y + dy[d]
        
        if xx < 0 or xx >= n or yy < 0 or yy >= n:
            continue
        
        if ch[xx][yy]:
            continue
        
        DFS(xx, yy, path)
        ch[xx][yy] = 0
        path.pop()
    
        
dx = [0, 1]
dy = [1, 0]

n = int(input())
board = [list(input().split()) for _ in range(n)]

ch = [[0 for _ in range(n)] for _ in range(n)]

mini = float('inf')
maxi = float('-inf')

DFS(0, 0, [])
print(maxi, mini)