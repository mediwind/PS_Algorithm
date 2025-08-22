import sys
import math

n = int(input().strip())
coins = list(map(int, input().split()))
coins.sort()
MAX = 100000

INF = 10**9
dp = [INF for _ in range(MAX + 1)]
dp[0] = 0
for c in coins:
    for v in range(c, MAX + 1):
        if dp[v - c] + 1 < dp[v]:
            dp[v] = dp[v - c] + 1

for x in range(1, MAX + 1):
    rem = x
    g = 0
    # greedy: 큰 동전부터
    for c in reversed(coins):
        if c <= rem:
            k = rem // c
            g += k
            rem -= k * c
            if rem == 0:
                break
    # dp[x]는 항상 정의됨(1이 있으므로)
    if g > dp[x]:
        print(x)
        sys.exit(0)

print(-1)