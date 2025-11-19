import sys
input = sys.stdin.readline

t = int(input().rstrip())
ans = []
for _ in range(t):
    n, m, k = map(int, input().rstrip().split())
    forbidden = [False] * (n + 1)
    for s in range(1, n+1):
        if s >= m and ((s - m) % k == 0):
            forbidden[s] = True
    dp = [0] * (n + 1)
    dp[0] = 1
    for x in range(1, n+1):
        tot = 0
        for length in range(1, x+1):
            if not forbidden[length]:
                tot += dp[x - length]
        dp[x] = tot
        
    print(dp[n])