from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx, sy):
    Q = deque()
    Q.append((sx, sy))
    ch[sx][sy] = 0
    
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx >= n + 1 or yy < 0 or yy >= m + 1:
                continue
            if 0 < xx < n and 0 < yy < m:
                continue
            if ch[xx][yy] == -1:
                Q.append((xx, yy))
                ch[xx][yy] = ch[x][y] + 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
m, n = map(int, input().split())
k = int(input())

board = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
ch = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
store = set()
for i in range(1, k + 2):
    a, b = map(int, input().split())
    if i == k + 1:
        if a == 1:
            board[0][b] = 0
        elif a == 2:
            board[n][b] = 0
        elif a == 3:
            board[b][0] = 0
        else:
            board[b][m] = 0
        continue
        
    if a == 1:
        board[0][b] = i
        store.add((0, b))
    elif a == 2:
        board[n][b] = i
        store.add((n, b))
    elif a == 3:
        board[b][0] = i
        store.add((b, 0))
    else:
        board[b][m] = i
        store.add((b, m))

for i in range(n + 1):
    for j in range(m + 1):
        if board[i][j] == 0:
            BFS(i, j)

ans = 0
for x, y in store:
    ans += ch[x][y]
print(ans)