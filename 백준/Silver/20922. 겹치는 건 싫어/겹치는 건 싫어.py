n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0 for _ in range(100001)]

lt = 0
rt = 0
res = 0

while lt < n:
    if cnt[arr[lt]] != k:
        cnt[arr[lt]] += 1
        lt += 1
    else:
        cnt[arr[rt]] -= 1
        rt += 1
    res = max(res, lt - rt)

print(res)