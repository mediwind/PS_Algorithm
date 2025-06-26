import sys
input = sys.stdin.readline


N = int(input().rstrip())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

dy = [[0 for _ in range(N)] for _ in range(N)]
dy[0][0] = board[0][0]

for i in range(1, N):
    # 첫 행 초기화
    dy[0][i] = dy[0][i - 1] * 2 + board[0][i]
    # 첫 열 초기화
    dy[i][0] = dy[i - 1][0] * 2 + board[i][0]

for i in range(1, N):
    for j in range(1, N):
        dy[i][j] = max(dy[i - 1][j], dy[i][j - 1]) * 2 + board[i][j]

print(dy[N - 1][N - 1])