from collections import deque
import sys
input = sys.stdin.readline

def BFS(n, m, board):
    ch = [[[False, False] for _ in range(m)] for _ in range(n)]
    Q = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                Q.append(((i, j), 0, 0))
                ch[i][j][0] = True

    while Q:
        (y, x), now_t, now_f = Q.popleft()

        if now_f == 1 and board[y][x] == 'H':
            return now_t

        for d in range(4):
            yy = y + dy[d]
            xx = x + dx[d]

            if 0 <= yy < n and 0 <= xx < m and not ch[yy][xx][now_f] and board[yy][xx] != 'D':
                if now_f == 0:
                    if board[yy][xx] == 'F':
                        Q.append(((yy, xx), now_t + 1, 1))
                        ch[yy][xx][1] = True
                    else:
                        Q.append(((yy, xx), now_t + 1, 0))
                        ch[yy][xx][0] = True
                else:
                    Q.append(((yy, xx), now_t + 1, 1))
                    ch[yy][xx][1] = True

    return -1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
print(BFS(n, m, board))