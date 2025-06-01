import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# dy[i][j][k]는 (i, j) 위치에 k 종류의 '이동 방식'으로 도착했을 때의 최소 누적 연료.
# k = 0: '오른쪽 아래 대각선' (↘) 이동으로 (i,j)에 도착. 이전 위치는 (i-1, j-1).
# k = 1: '아래' (↓) 이동으로 (i,j)에 도착. 이전 위치는 (i-1, j).
# k = 2: '왼쪽 아래 대각선' (↙) 이동으로 (i,j)에 도착. 이전 위치는 (i-1, j+1).
dy = [[[0 for _ in range(3)] for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dy[0][j][k] = board[0][j]

for i in range(1, n):
    for j in range(m):
        # k = 0: (i,j)에 '오른쪽 아래 대각선' (↘) 이동으로 도착한 경우. 이전 칸은 (i-1, j-1).
        # 이전 칸 (i-1, j-1)에서는 '아래'(1) 또는 '왼쪽 아래 대각선'(2) 이동만 가능했음.
        if j > 0: # (i-1, j-1)이 유효한 경우 (가장 왼쪽 열이 아님)
            dy[i][j][0] = board[i][j] + min(dy[i - 1][j - 1][1], dy[i - 1][j - 1][2])
        else: # (i-1, j-1)에서 올 수 없는 경우 (가장 왼쪽 열)
            dy[i][j][0] = float('inf')
        
        # k = 1: (i,j)에 '아래' (↓) 이동으로 도착한 경우. 이전 칸은 (i-1, j).
        # 이전 칸 (i-1, j)에서는 '오른쪽 아래 대각선'(0) 또는 '왼쪽 아래 대각선'(2) 이동만 가능했음.
        dy[i][j][1] = board[i][j] + min(dy[i - 1][j][0], dy[i - 1][j][2])
        
        # k = 2: (i,j)에 '왼쪽 아래 대각선' (↙) 이동으로 도착한 경우. 이전 칸은 (i-1, j+1).
        # 이전 칸 (i-1, j+1)에서는 '오른쪽 아래 대각선'(0) 또는 '아래'(1) 이동만 가능했음.
        if j < m - 1: # (i-1, j+1)이 유효한 경우 (가장 오른쪽 열이 아님)
            dy[i][j][2] = board[i][j] + min(dy[i - 1][j + 1][0], dy[i - 1][j + 1][1])
        else: # (i-1, j+1)에서 올 수 없는 경우 (가장 오른쪽 열)
            dy[i][j][2] = float('inf')

ans = float('inf')
for j in range(m):
    ans = min(ans, min(dy[n - 1][j]))

print(ans)