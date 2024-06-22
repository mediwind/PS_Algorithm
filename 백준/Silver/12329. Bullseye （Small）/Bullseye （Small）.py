import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    r, t = map(int, input().split())

    def infeasible(x):
        return (x + 1) * (2 * r + 2 * x + 1) > t

    def binary_search(hi):
        lo = 0
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if infeasible(mid):
                hi = mid
            else:
                lo = mid + 1
        if not infeasible(lo):
            return -1
        return lo

    limit = 1e18 // r
    limit = min(limit, 1e9)
    ans = binary_search(limit)
    print(f"Case #{i}: {int(ans)}")