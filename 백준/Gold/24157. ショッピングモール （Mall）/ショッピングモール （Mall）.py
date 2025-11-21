import sys
input = sys.stdin.readline
m, n = map(int, input().rstrip().split())
a, b = map(int, input().rstrip().split())

sum_cost = [[0] * (m + 1) for _ in range(n + 1)]
sum_block = [[0] * (m + 1) for _ in range(n + 1)]

for r in range(1, n + 1):
    row = list(map(int, input().rstrip().split()))
    row_sum = 0
    row_block = 0
    for c in range(1, m + 1):
        val = row[c - 1]
        if val == -1:
            row_block += 1
            val_cost = 0
        else:
            val_cost = val
        row_sum += val_cost
        
        sum_cost[r][c] = sum_cost[r - 1][c] + row_sum
        sum_block[r][c] = sum_block[r - 1][c] + row_block

INF = 10**18
ans = INF

max_r = n - b + 1
max_c = m - a + 1
for r in range(1, max_r + 1):
    r2 = r + b - 1
    for c in range(1, max_c + 1):
        c2 = c + a - 1
        blocks = (sum_block[r2][c2] - sum_block[r - 1][c2]
                  - sum_block[r2][c - 1] + sum_block[r - 1][c - 1])
        if blocks > 0:
            continue
        total = (sum_cost[r2][c2] - sum_cost[r - 1][c2]
                 - sum_cost[r2][c - 1] + sum_cost[r - 1][c - 1])
        if total < ans:
            ans = total

print(ans)