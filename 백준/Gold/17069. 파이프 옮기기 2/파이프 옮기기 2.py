n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [[[0, 0, 0] for _ in range(n)] for _ in range(n)] # [x][y][0] = 가로, [x][y][1] = 세로, [x][y][2] = 대각선

dy[0][1][0] = 1 # board의 [0][1]에 파이프의 끝이 가로로 놓여 있으므로 1 표시
for i in range(1, n): # 첫번째 행은 무조건 가로로만 놓을 수 있으므로 1로 초기화
    if board[0][i]: # 도중에 벽(1)을 만나면 가로로 더 진행할 수 없으므로 break
        break
    dy[0][i][0] = 1

for i in range(1, n):
    for j in range(2, n):
        if not board[i][j]: # 가로나 세로로 파이프를 옮길 때는 파이프의 끝이 놓일 한칸만 비어있으면 된다.
            dy[i][j][0] = dy[i][j-1][0] + dy[i][j-1][2] # 가로
            dy[i][j][1] = dy[i-1][j][1] + dy[i-1][j][2] # 세로
        if not board[i-1][j] and not board[i][j-1] and not board[i][j]: # 대각선의 경우는 세칸이 비어있어야 한다.
            dy[i][j][2] = dy[i-1][j-1][0] + dy[i-1][j-1][1] + dy[i-1][j-1][2] # 대각선

print(sum(dy[n-1][n-1]))