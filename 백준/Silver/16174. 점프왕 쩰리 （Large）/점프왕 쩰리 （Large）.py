import sys
input = sys.stdin.readline

n = int(input().rstrip())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[False] * n for _ in range(n)]
dp[0][0] = True

for i in range(n):
    for j in range(n):
        if dp[i][j]:
            jump = board[i][j]
            if jump == -1:
                print("HaruHaru")
                sys.exit(0)

            if i + jump < n:
                dp[i + jump][j] = True
            if j + jump < n:
                dp[i][j + jump] = True

print("Hing")