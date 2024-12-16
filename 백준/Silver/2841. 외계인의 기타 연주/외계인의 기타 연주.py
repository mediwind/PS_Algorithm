from collections import defaultdict
import sys
input = sys.stdin.readline

line = defaultdict(list)
n, p = map(int, input().split())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    while line[a] and line[a][-1] > b:
        line[a].pop()
        ans += 1
    if not line[a] or line[a][-1] < b:
        line[a].append(b)
        ans += 1

print(ans)