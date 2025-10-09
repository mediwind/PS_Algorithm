import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ans = n + 1
    if n >= 1:
        ans += (n - 1) * 2 + (n - 2) * (n - 1)
    if n >= 2:
        ans += max(n - 2, 0) + (n - 3) * (n - 2)
    print(ans)