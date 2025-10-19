import sys
input = sys.stdin.readline


def cumulative(n: int) -> int:
    q, r = divmod(n, 3)
    return (3 * q * (q + 1)) // 2 + r * (q + 1)


t = int(input().rstrip())
for _ in range(t):
    N = int(input().rstrip())
    limit = (N + 2) // 3
    lo, hi = 0, 1
    
    while cumulative(hi) <= limit:
        hi <<= 1
        
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cumulative(mid) <= limit:
            lo = mid
        else:
            hi = mid - 1
            
    print(lo + 1)