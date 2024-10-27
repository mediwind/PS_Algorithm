n, x = map(int, input().split())
arr = list(map(int, input().split()))

lt, rt = 0, x - 1
tmp = sum(arr[lt:rt + 1]) if len(arr) >= 2 else arr[lt]
ans = tmp
cnt = {tmp: 1}
while True:
    tmp -= arr[lt]
    lt += 1
    rt += 1
    if rt >= n:
        break
    tmp += arr[rt]
    cnt[tmp] = cnt.get(tmp, 0) + 1
    ans = max(ans, tmp)

if not ans:
    print("SAD")
else:
    print(ans)
    print(cnt[ans])