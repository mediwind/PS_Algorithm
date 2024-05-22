def simulation(hour):
    for work in works:
        hour += work[0]
        if hour > work[1]:
            return False
    return True

N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
works.sort(key=lambda x: (x[1], x[0]))

ans = -1
lt, rt = 0, works[0][1] - works[0][0]
while lt <= rt:
    mid = (lt + rt) // 2
    if simulation(mid):
        lt = mid + 1
        ans = mid
    else:
        rt = mid - 1

print(ans)