import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# dy[i][j][k]는 (i, j) 위치에 k 방향으로 도착했을 때의 최소 연료 소모량
# k = 0: 왼쪽 아래 대각선에서 옴 (이전 위치: (i-1, j-1))
# k = 1: 바로 아래에서 옴 (이전 위치: (i-1, j))
# k = 2: 오른쪽 아래 대각선에서 옴 (이전 위치: (i-1, j+1))
dy = [[[0 for _ in range(3)] for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dy[0][j][k] = board[0][j]

for i in range(1, n):
    for j in range(m):
        for k in range(3): # 방향 k에 대해 계산
            if k == 0: # 현재 (i, j)에 왼쪽 아래 대각선(0)으로 도착한 경우
                if j > 0:
                    dy[i][j][k] = board[i][j] + min(dy[i - 1][j - 1][1], dy[i - 1][j - 1][2])
                else: # 가장 왼쪽 열이라 왼쪽에서 올 수 없음
                    dy[i][j][k] = float('inf')
            
            elif k == 1: # 현재 (i, j)에 바로 아래(1)로 도착한 경우
                dy[i][j][k] = board[i][j] + min(dy[i - 1][j][0], dy[i - 1][j][2])
            
            else: # k == 2, 현재 (i, j)에 오른쪽 아래 대각선(2)으로 도착한 경우
                if j < m - 1:
                    dy[i][j][k] = board[i][j] + min(dy[i - 1][j + 1][0], dy[i - 1][j + 1][1])
                else: # 가장 오른쪽 열이라 오른쪽에서 올 수 없음
                    dy[i][j][k] = float('inf')

ans = float('inf')
for j in range(m):
    ans = min(ans, min(dy[n - 1][j]))

print(ans)