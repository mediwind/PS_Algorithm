n, m = map(int, input().split())
arr = list(range(1, n + 1))

for _ in range(m):
    st, ed = map(int, input().split())
    arr[st - 1:ed] = arr[st - 1:ed][::-1]

print(*arr)