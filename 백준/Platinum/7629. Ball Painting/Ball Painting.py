import sys
# input = sys.stdin.readline
MOD = 1_000_000_007

MAXN = 1000
dp = [0] * (MAXN + 1)

# 기저 조건: N = 1일 때
dp[1] = 2

# 점화식: P(N) = P(N-1) * 4 * (2N - 1)
for i in range(2, MAXN + 1):
    dp[i] = (dp[i - 1] * 4 * (2 * i - 1)) % MOD

while True:
    line = input().strip()
    if not line:
        break
        
    n = int(line)
    
    # 종료 조건
    if n == 0:
        break
        
    print(dp[n])