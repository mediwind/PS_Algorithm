import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

dy = [[[float('inf') for _ in range(3)] for _ in range(M)] for _ in range(N)]
for j in range(M):
    for d in range(3):
        dy[0][j][d] = board[0][j]

for i in range(1, N):
    for j in range(M):
        for d in range(3):
            prev_j = j + (d - 1)
            if 0 <= prev_j < M:
                for prev_d in range(3):
                    if d != prev_d:
                        dy[i][j][d] = min(dy[i][j][d], dy[i - 1][prev_j][prev_d] + board[i][j])

ans = float('inf')
for j in range(M):
    for d in range(3):
        ans = min(ans, dy[N - 1][j][d])
print(ans)