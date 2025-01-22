def check(mid):
    if arr[1] - arr[0] > mid:
        return False
    if arr[-1] - arr[-2] > mid:
        return False
    
    for i in range(2, len(arr) - 2):
        if (arr[i + 1] - arr[i]) / 2 > mid:
            return False
    
    return True


N = int(input())
M = int(input())
arr = [0] + list(map(int, input().split())) + [N]

lt, rt = 0, N
ans = float("inf")
while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid):
        rt = mid - 1
        ans = min(ans, mid)
    else:
        lt = mid + 1
print(ans)