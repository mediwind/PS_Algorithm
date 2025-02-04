N, M, X = map(int, input().split())
goods = list(map(int, input().split()))

ans = [0 for _ in range(M)]
for i in range(M):
    good = goods[i]
    lt, rt = 1, N
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if X - (mid * good) >= (N - mid) * goods[-1]:
            lt = mid + 1
            res = max(res, mid)
        else:
            rt = mid - 1
    
    ans[i] += res
    X -= (res * good)
    N -= res

print(*ans)