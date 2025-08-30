def check(max_wait):
    bus_count = 1
    cow_count = 1
    first_cow_time = times[0]
    
    for i in range(1, N):
        if times[i] - first_cow_time > max_wait or cow_count == C:
            bus_count += 1
            cow_count = 1
            first_cow_time = times[i]
        else:
            cow_count += 1
    
    return bus_count <= M


N, M, C = map(int, input().split())
times = sorted(list(map(int, input().split())))

ans = float('inf')
lt, rt = 0, times[-1] - times[0]
while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid):
        ans = min(ans, mid)
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)