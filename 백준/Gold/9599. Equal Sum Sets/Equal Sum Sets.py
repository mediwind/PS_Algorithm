import sys
input = sys.stdin.readline

while True:
    n, k, s = map(int, input().rstrip().split())
    
    if n == 0 and k == 0 and s == 0:
        break
        
    # dp[i][j][k]: 1 ~ i까지에서 j개를 골라 합이 k인 경우의 수
    dp = [[[0 for _ in range(s + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(0, k + 1):
            for t in range(0, s + 1):
                # i를 안 고르는 경우
                dp[i][j][t] = dp[i - 1][j][t]
                # i를 고르는 경우
                if j > 0 and t >= i:
                    dp[i][j][t] += dp[i - 1][j - 1][t - i]
    
    print(dp[n][k][s])