import math
import sys
input = sys.stdin.readline

def belong_group(x, y, n, m, g):
    if x == 1:
        return (y-1) // (n//g)
    else:
        return (y-1) // (m//g)

n, m, q = map(int, input().rstrip().split())
g = math.gcd(n, m)
for _ in range(q):
    sx, sy, ex, ey = map(int, input().rstrip().split())
    print("YES" if belong_group(sx, sy, n, m, g) == belong_group(ex, ey, n, m, g) else "NO")