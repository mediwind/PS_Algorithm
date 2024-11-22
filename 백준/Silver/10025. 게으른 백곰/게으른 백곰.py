import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])

now = 0
maxi = 0
left = 0

for right in range(n):
    now += arr[right][0]

    while arr[right][1] - arr[left][1] > 2 * k:
        now -= arr[left][0]
        left += 1

    if now > maxi:
        maxi = now

print(maxi)