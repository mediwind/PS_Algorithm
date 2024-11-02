n, k = map(int, input().split())
arr = list(map(int, input().split()))

lion = list()
for i in range(n):
    if arr[i] == 1:
        lion.append(i)

if len(lion) < k:
    print(-1)
else:
    ans = float('inf')
    lt, rt = 0, k - 1
    for i in range(len(lion) - k + 1):
        ans = min(ans, lion[rt] - lion[lt] + 1)
        lt += 1
        rt += 1
    print(ans)