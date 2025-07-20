import sys
input = sys.stdin.readline

P = int(input().rstrip())
for _ in range(P):
    K, n, m, k = map(int, input().rstrip().split())
    
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    
    S = set()
    num = m
    while num <= n:
        S.add(num)
        num += k
    
    for x in range(1, n + 1):
        for t in range(1, x + 1):
            if t not in S:
                dp[x] += dp[x - t]
    
    print(f"{K} {dp[n]}")