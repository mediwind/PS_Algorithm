def flip_over(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            if board[i][j] == 1:
                board[i][j] = 0
            else:
                board[i][j] = 1


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
# board

cnt = 0
for x in range(N - 1, -1, -1):
    for y in range(N - 1, -1, -1):
        if board[x][y] == 1:
            flip_over(x, y)
            cnt += 1
#             print(x, y)
#             for bd in board:
#                 print(bd)
#             print()

print(cnt)