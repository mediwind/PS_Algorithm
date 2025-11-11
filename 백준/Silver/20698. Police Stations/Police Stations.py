import sys
input = sys.stdin.readline

n = int(input().rstrip().strip())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    xs.append(x)
    ys.append(y)

dx = max(xs) - min(xs)
dy = max(ys) - min(ys)
L = (dx + 1) // 2
W = (dy + 1) // 2

print(L, W)