import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
grid = [input().rstrip() for _ in range(n)]

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    row = grid[i]
    for j in range(n):
        val = 1 if row[j] == 'D' else 0
        prefix_sum[i + 1][j + 1] = (
            prefix_sum[i + 1][j]
            + prefix_sum[i][j + 1]
            - prefix_sum[i][j]
            + val
        )

max_cells = s * s
counts = [0] * (max_cells + 1)
limit = n - s + 1
for r in range(limit):
    r1 = r
    r2 = r + s
    for c in range(limit):
        c1 = c
        c2 = c + s
        dirty = (
            prefix_sum[r2][c2]
            - prefix_sum[r1][c2]
            - prefix_sum[r2][c1]
            + prefix_sum[r1][c1]
        )
        counts[dirty] += 1

output = []
for k, v in enumerate(counts):
    if v:
        output.append(f"{k} {v}")

print("\n".join(output))