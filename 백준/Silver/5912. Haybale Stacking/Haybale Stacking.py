import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0 for _ in range(n + 2)]
for _ in range(k):
    s, e = map(int, input().split())
    arr[s] += 1
    arr[e + 1] -= 1
# arr

prefix = [0 for _ in range(n + 2)]
total = 0
for i in range(1, n + 2):
    prefix[i] = arr[i] + total
    total += arr[i]
# prefix

print(sorted(prefix[1:n + 1])[n // 2])