import sys
input = sys.stdin.readline
INF = 10**18

C, R, B = map(int, input().split())

x = []
y = []
price = []

for _ in range(R):
    data = list(map(int, input().split()))
    x.append(data[0])
    y.append(data[1])
    price.append(data[2:])

dist = [[0]*R for _ in range(R)]
for i in range(R):
    for j in range(R):
        dist[i][j] = abs(x[i]-x[j]) + abs(y[i]-y[j])

dp = [[[INF]*(B+1) for _ in range(R)] for __ in range(C+1)]

for k in range(R):
    p = price[k][0]
    if p > 0 and p <= B:
        dp[1][k][p] = 0

for c in range(2, C+1):
    for k in range(R):
        p = price[k][c-1]
        if p == 0:
            continue

        for b in range(p, B+1):
            prev_budget = b - p

            for prev in range(R):
                if dp[c-1][prev][prev_budget] == INF:
                    continue

                dp[c][k][b] = min(
                    dp[c][k][b],
                    dp[c-1][prev][prev_budget] + dist[prev][k]
                )

ans = INF
for k in range(R):
    for b in range(B+1):
        ans = min(ans, dp[C][k][b])

print(-1 if ans == INF else ans)