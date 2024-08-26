def check(idx):
    location = homes[idx]
    res = 0
    for home in homes:
        res += abs(location - home)
        
    return res


n = int(input())
homes = list(map(int, input().split()))
homes.sort()

lt, rt = 0, n - 1
res = float("inf")
while lt <= rt:
    mid = (lt + rt) // 2
    dist = check(mid)
    if dist <= res:
        rt = mid - 1
        res = min(res, dist)
        ans = mid
    else:
        lt = mid + 1

print(homes[ans])