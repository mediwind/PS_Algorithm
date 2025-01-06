import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

diff = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b, k = map(int, input().split())
    diff[a - 1] += k
    diff[b] -= k

current = 0
for i in range(N):
    current += diff[i]
    heights[i] += current

print(*heights)