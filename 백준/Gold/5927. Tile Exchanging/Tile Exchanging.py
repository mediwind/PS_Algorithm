import sys
input = sys.stdin.readline

INF = 10**18

n, M = map(int, input().rstrip().split())
tiles = [int(input().rstrip()) for _ in range(n)]
limit = int(M**0.5)

dp = [INF] * (M + 1)
dp[0] = 0

for a in tiles:
    nxt = [INF] * (M + 1)
    for s in range(M + 1):
        if dp[s] == INF:
            continue
        for b in range(limit + 1):
            area = b * b
            if s + area > M:
                continue
            cost = dp[s] + (a - b) * (a - b)
            if cost < nxt[s + area]:
                nxt[s + area] = cost
    dp = nxt

print(dp[M] if dp[M] != INF else -1)