import sys
import math
input = sys.stdin.readline

N = int(input().strip())
L, W = map(int, input().strip().split())

P = []
for _ in range(N):
    P.append(int(input().strip()))

P.sort()

M = N // 2

target_x = [i * L / (M - 1) for i in range(M)]

INF = float('inf')
dp = [[INF] * (M + 1) for _ in range(M + 1)]

dp[0][0] = 0.0

for l in range(M + 1):
    for r in range(M + 1):
        if l == 0 and r == 0:
            continue
            
        idx = l + r - 1
        
        if l > 0:
            dist_left = abs(P[idx] - target_x[l - 1])
            dp[l][r] = min(dp[l][r], dp[l - 1][r] + dist_left)
            
        if r > 0:
            dist_right = math.hypot(P[idx] - target_x[r - 1], W)
            dp[l][r] = min(dp[l][r], dp[l][r - 1] + dist_right)

print(f"{dp[M][M]:.10f}")