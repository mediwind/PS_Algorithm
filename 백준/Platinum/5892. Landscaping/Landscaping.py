import sys
input = sys.stdin.readline

N, X, Y, Z = map(int, input().strip().split())

A = []
B = []

for i in range(N):
    current_dirt, target_dirt = map(int, input().split())
    if current_dirt > target_dirt:
        for _ in range(current_dirt - target_dirt):
            A.append(i)
    elif current_dirt < target_dirt:
        for _ in range(target_dirt - current_dirt):
            B.append(i)

len_a = len(A)
len_b = len(B)

INF = float('inf')
dp = [[INF] * (len_b + 1) for _ in range(len_a + 1)]

dp[0][0] = 0

for i in range(1, len_a + 1):
    dp[i][0] = i * Y

for j in range(1, len_b + 1):
    dp[0][j] = j * X

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        cost_remove = dp[i-1][j] + Y
        
        cost_add = dp[i][j-1] + X
        
        dist = abs(A[i-1] - B[j-1])
        cost_move = dp[i-1][j-1] + Z * dist
        
        dp[i][j] = min(cost_remove, cost_add, cost_move)

print(dp[len_a][len_b])