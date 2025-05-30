n = int(input().strip())

dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
    dp[i] = sum(dp[j] * dp[i - 1 - j] for j in range(i))

print(dp[n])