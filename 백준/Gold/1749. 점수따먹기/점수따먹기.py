import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

col_sum = [[0 for _ in range(M)] for _ in range(N + 1)]
for r in range(1, N + 1):
    for c in range(M):
        col_sum[r][c] = col_sum[r - 1][c] + matrix[r - 1][c]

ans = float('-inf')

for r1 in range(1, N + 1):
    for r2 in range(r1, N + 1):
        
        prev_dp = 0
        for c in range(M):
            val = col_sum[r2][c] - col_sum[r1 - 1][c]
            
            if c == 0:
                curr_dp = val
            else:
                curr_dp = max(prev_dp + val, val)
            
            if curr_dp > ans:
                ans = curr_dp
            prev_dp = curr_dp

print(ans)