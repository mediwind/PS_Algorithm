import sys
input = sys.stdin.readline

N = int(input().rstrip())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [[float('inf') for _ in range(N)] for _ in range(N)]
dp[0][0] = 0

for i in range(N):
    for j in range(N):
        cur_val = board[i][j]
        cur_cost = dp[i][j]
        
        # 아래로 이동 가능
        if i + 1 < N:
            additional_cost = max(0, board[i + 1][j] - cur_val + 1)
            dp[i + 1][j] = min(dp[i + 1][j], cur_cost + additional_cost)
        
        # 우측으로 이동 가능
        if j + 1 < N:
            additional_cost = max(0, board[i][j + 1] - cur_val + 1)
            dp[i][j + 1] = min(dp[i][j + 1], cur_cost + additional_cost)

print(dp[-1][-1])