import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    board[i][i] = 0

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    board[a][b] = 1
    board[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

ans = (float('inf'), 0, 0)
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        total = 0
        for x in range(1, N + 1):
            total += min(board[x][i], board[x][j]) * 2
            
        if total > ans[0]:
            continue

        if total < ans[0]:
            ans = (total, i, j)
            continue

        if i < ans[1]:
            ans = (total, i, j)
            continue

        if i == ans[1] and j < ans[2]:
            ans = (total, i, j)

print(ans[1], ans[2], ans[0])