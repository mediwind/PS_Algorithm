n = int(input())
board = [[float('inf') for _ in range(26)] for _ in range(26)]
for _ in range(n):
    a, b = map(lambda x: ord(x) - 97, input().split(' is '))
    board[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

m = int(input())
for _ in range(m):
    a, b = map(lambda x: ord(x) - 97, input().split(' is '))
    if board[a][b] == float('inf'):
        print('F')
    else:
        print('T')