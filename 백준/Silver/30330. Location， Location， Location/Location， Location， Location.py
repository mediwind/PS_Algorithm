import sys
input = sys.stdin.readline

n = int(input().rstrip())
xs, ys = [], []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

mx = xs[(n - 1) // 2]
my = ys[(n - 1) // 2]

print(mx, my)