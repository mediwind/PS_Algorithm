def how_many(x):
#     print('in func x:', x)
    cnt = 1
    max_x, min_x = arr[0], arr[0]
    
    for i in range(1, n):
        max_x = max(max_x, arr[i])
        min_x = min(min_x, arr[i])
        
        if max_x - min_x > x:
#             print('i:', i)
            cnt += 1
            max_x, min_x = arr[i], arr[i]
    
    return cnt


n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt, rt = 0, max(arr)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = how_many(mid)
#     print(lt, rt, res)
    if res <= m:
        rt = mid - 1
        ans = mid
    else:
        lt = mid + 1
print(ans)