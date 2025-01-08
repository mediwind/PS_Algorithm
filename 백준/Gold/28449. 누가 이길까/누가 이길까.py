def bisect_left(x):
    lt, rt = 0, m - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if x > arc[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    
    return lt


n, m = map(int, input().split())
hi = sorted(list(map(int, input().split())))
arc = sorted(list(map(int, input().split())))

ans = [0 for _ in range(3)]
for h in hi:
    a = bisect_left(h)
    b = bisect_left(h + 1)
    # HI팀 승리 횟수
    ans[0] += a
    # 무승부 횟수
    ans[2] += b - a

# ARC팀 승리 횟수
ans[1] = (n * m) - ans[0] - ans[2]
print(*ans)