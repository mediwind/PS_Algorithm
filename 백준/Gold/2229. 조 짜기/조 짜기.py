n = int(input())
arr = list(map(int, input().split()))
dy = [0 for _ in range(n + 1)]

for i in range(n):
    mx = mn = arr[i]
    for j in range(i, -1, -1):
        mx = max(mx, arr[j])
        mn = min(mn, arr[j])
        dy[i + 1] = max(dy[i + 1], dy[j] + mx - mn)

print(dy[n])