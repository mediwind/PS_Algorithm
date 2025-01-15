S = input().strip()
P = input().strip()

n, m = len(S), len(P)
dp = [float('inf')] * (m + 1)
dp[0] = 0

for i in range(m):
    for j in range(i + 1, m + 1):
        if P[i:j] in S:
            dp[j] = min(dp[j], dp[i] + 1)

print(dp[m])