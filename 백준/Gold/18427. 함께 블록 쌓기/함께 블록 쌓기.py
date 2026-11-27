import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    blocks = students[i - 1]
    for h in range(H + 1):
        dp[i][h] = dp[i - 1][h]
        
        for b in blocks:
            if h >= b:
                dp[i][h] += dp[i - 1][h - b]
        
        dp[i][h] %= 10007

print(dp[N][H])