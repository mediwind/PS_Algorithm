import math

N = int(input().strip())
def C(n, k):
    if n < k or k < 0:
        return 0
    return math.comb(n, k)

total = C(N - 1, 3)
M = (N + 1) // 2
bad_each = C(N - M, 3)
ans = total - 4 * bad_each
print(ans)