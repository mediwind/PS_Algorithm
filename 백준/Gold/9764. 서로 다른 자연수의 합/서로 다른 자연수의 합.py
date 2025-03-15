import sys
input = sys.stdin.readline

t = int(input().rstrip())
dp = [1] + [0] * 2000

for i in range(1, 2001):
    for j in range(2000, i - 1, -1):
        dp[j] = (dp[j] + dp[j - i]) % 100999

for _ in range(t):
    n = int(input().rstrip())
    print(dp[n])