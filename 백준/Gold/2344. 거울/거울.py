from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx, sy, d):
    if board[sx][sy] == 1:
        d = (d + 2) % 4
    Q = deque()
    Q.append((sx, sy))
    
    while Q:
        x, y = Q.popleft()
        xx = x + move[d][0]
        yy = y + move[d][1]
        
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            if yy == -1:
                return x + 1
            elif xx == n:
                return x + (y + 1)
            elif yy == m:
                return (2 * n + m) - x
            elif xx == -1:
                return (2 * n + 2 * m) - y
        
        if board[xx][yy] == 1:
            d = (d + 2) % 4
        Q.append((xx, yy))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

move = [(0, -1), (0, 1), (1, 0), (-1, 0)]

ans = [-1 for _ in range(2 * n + 2 * m + 1)]
cnt = 1
for i in range(n):
    res = BFS(i, 0, 1)
    ans[cnt] = res
    ans[res] = cnt
    cnt += 1

for j in range(m):
    res = BFS(n - 1, j, 3)
    ans[cnt] = res
    ans[res] = cnt
    cnt += 1

print(*ans[1:])