import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a, b = map(int, input().rstrip().split())
grid = [input().rstrip() for _ in range(n)]

ans = 10**18
max_k = min(n, m) // 3

for k in range(1, max_k + 1):
    h = w = 3 * k
    for r0 in range(n - h + 1):
        for c0 in range(m - w + 1):
            cost = 0
            stop_outer = False
            for i in range(n):
                if cost >= ans:
                    stop_outer = True
                    break
                row = grid[i]
                for j in range(m):
                    target = 0
                    if r0 <= i < r0 + h and c0 <= j < c0 + w:
                        di = i - r0
                        dj = j - c0
                        if di < k or dj < k or di >= 2 * k:
                            target = 1
                    if row[j] == '#':
                        if target == 0:
                            cost += b
                    else:
                        if target == 1:
                            cost += a
                    if cost >= ans:
                        break
            if stop_outer:
                continue
            if cost < ans:
                ans = cost

print(ans)