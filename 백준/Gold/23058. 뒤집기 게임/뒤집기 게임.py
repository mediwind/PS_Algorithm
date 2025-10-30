import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 10**9
for mask in range(1 << n):
    row_cost = bin(mask).count("1")
    cost0 = row_cost
    cost1 = row_cost
    for c in range(n):
        ones = 0
        for r in range(n):
            v = board[r][c]
            if (mask >> r) & 1:
                v ^= 1
            ones += v
        zeros = n - ones
        cost0 += min(ones, 1 + zeros)
        cost1 += min(zeros, 1 + ones)
        if cost0 >= ans and cost1 >= ans:
            break
    ans = min(ans, cost0, cost1)

print(ans)