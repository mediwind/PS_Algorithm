import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()

lt, rt = 1, max(arr)
ans = float('inf')

while lt <= rt:
    mid = (lt + rt) // 2

    a, b = 0, 0

    for i in range(N):
        if arr[i] < mid:
            a += arr[i]
        elif arr[i] > mid:
            b += arr[i]

    if a >= b:
        ans = min(ans, mid)
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)