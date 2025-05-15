n = int(input())
arr = list(map(int, input().split()))

dy = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dy[i] = max(dy[i], dy[j] + 1)

print(n - max(dy))