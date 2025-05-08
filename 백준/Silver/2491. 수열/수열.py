n = int(input())
arr = list(map(int, input().split()))

dy_bigger = [1 for _ in range(n)]
for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        dy_bigger[i] = dy_bigger[i - 1] + 1

dy_smaller = [1 for _ in range(n)]
for i in range(1, n):
    if arr[i - 1] >= arr[i]:
        dy_smaller[i] = dy_smaller[i - 1] + 1

print(max(max(dy_bigger), max(dy_smaller)))