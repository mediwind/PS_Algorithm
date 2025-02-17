import sys
input = sys.stdin.readline

n = int(input().strip())

start = dict()
for _ in range(n):
    x, t, c = map(int, input().strip().split())
    start[x - t] = start.get(x - t, 0) + c

print(max(start.values()))