def minimum_is(x):
    cnt, curr = 0, 0
    for num in arr:
        curr += num
        if curr >= x:
            cnt += 1
            curr = 0
    
    return cnt >= K

N, K = map(int, input().split())
arr = list(map(int, input().split()))

lt, rt = 0, sum(arr)
while lt <= rt:
    mid = (lt + rt) // 2
    if minimum_is(mid):
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)