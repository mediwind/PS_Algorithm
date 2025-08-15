n, c = map(int, input().split())
coins = [int(input()) for _ in range(c)]

dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]
for j in range(c + 1):
    dp[0][j] = 1

for i in range(1, n + 1):
    for j in range(1, c + 1):
        # j번째 동전을 사용하지 않는 경우
        dp[i][j] = dp[i][j-1]

        # j번째 동전을 사용하는 경우
        if i - coins[j-1] >= 0:
            dp[i][j] += dp[i - coins[j-1]][j]

print(dp[n][c])