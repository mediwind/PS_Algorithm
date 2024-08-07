n, m = map(int, input().split())
times = sorted(list(map(int, input().split())))

lt, rt = 1, times[-1] * m
ans = float('inf')
while lt <= rt:
    mid = (lt + rt) // 2
    
    balloons = 0
    for time in times:
        balloons += (mid // time)
        if balloons >= m:
            break
    
    if balloons >= m:
        ans = min(ans, mid)
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)