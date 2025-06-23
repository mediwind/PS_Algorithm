n = int(input())

arr = [1 for _ in range(n + 1)]
for i in range(4, n + 1):
    arr[i] = arr[i - 3] + arr[i - 1]

print(arr[n])