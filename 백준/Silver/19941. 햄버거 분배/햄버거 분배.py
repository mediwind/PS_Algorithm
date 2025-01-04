n, k = map(int, input().split())
arr = input().strip()

cnt = 0
arr = list(arr)

for i in range(n):
    if arr[i] != 'P':
        continue

    for j in range(i - k, i + k + 1):
        if 0 <= j < n and arr[j] == 'H':
            arr[j] = '-'
            cnt += 1
            break

print(cnt)