import sys
input = sys.stdin.readline


def can(g):
    total = 0
    for x in A:
        total += min(x, g)
        if total >= g * K:
            return True
    return False


N, K = map(int, input().split())
A = list(map(int, input().split()))

lo, hi = 0, sum(A) // K
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)