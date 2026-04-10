import sys
input = sys.stdin.readline

n, k = map(int, input().split())
r = [int(input()) for _ in range(n)]

INF = 10**30
ans = INF

for start in range(n):

    a = r[start:] + r[:start]

    # cost[s][e]
    cost = [[0]*n for _ in range(n)]

    for s in range(n):
        dist = 0
        for e in range(s, n):
            dist += a[e] * (e - s)
            cost[s][e] = dist

    dp = [[INF]*(n+1) for _ in range(k+1)]
    dp[0][0] = 0

    for d in range(1, k+1):
        for i in range(1, n+1):
            for j in range(i):
                dp[d][i] = min(
                    dp[d][i],
                    dp[d-1][j] + cost[j][i-1]
                )

    ans = min(ans, dp[k][n])

print(ans)