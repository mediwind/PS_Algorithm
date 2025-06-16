import sys
input = sys.stdin.readline


def get_prefix_sum(board):
    S = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            S[i][j] = board[i - 1][j - 1] + S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1]
    
    return S


N, M = map(int, input().split())
K = int(input())
board = [list(input()) for _ in range(N)]

M_j = [[0 for _ in range(M)] for _ in range(N)]
M_o = [[0 for _ in range(M)] for _ in range(N)]
M_i = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'J':
            M_j[i][j] = 1
        elif board[i][j] == 'O':
            M_o[i][j] = 1
        else:
            M_i[i][j] = 1

S_j = get_prefix_sum(M_j)
S_o = get_prefix_sum(M_o)
S_i = get_prefix_sum(M_i)

# S_j
# S_o
# S_i
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    
    jungle = S_j[x2][y2] - S_j[x1 - 1][y2] - S_j[x2][y1 - 1] + S_j[x1 - 1][y1 - 1]
    ocean = S_o[x2][y2] - S_o[x1 - 1][y2] - S_o[x2][y1 - 1] + S_o[x1 - 1][y1 - 1]
    ice = S_i[x2][y2] - S_i[x1 - 1][y2] - S_i[x2][y1 - 1] + S_i[x1 - 1][y1 - 1]
    
    print(jungle, ocean, ice)