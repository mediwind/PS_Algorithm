import sys
input = sys.stdin.readline

N = int(input().rstrip())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
prefix_sum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + board[i - 1][j - 1]

ans = float('-inf')
for k in range(1, N + 1):
    for i in range(k, N + 1):
        for j in range(k, N + 1):
            total = prefix_sum[i][j] - prefix_sum[i - k][j] - prefix_sum[i][j - k] + prefix_sum[i - k][j - k]
            ans = max(ans, total)

print(ans)