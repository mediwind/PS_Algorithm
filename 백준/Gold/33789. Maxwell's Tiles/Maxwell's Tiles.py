import sys
# input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input().strip())

pref = [1]
cur_s = 0
pow2 = pow(2, 4, MOD)
powstep = pow(2, 8, MOD)

for _ in range(t):
    m, n = map(int, input().strip().split())
    s = min(m, n)
    d = abs(m - n)
    while cur_s < s:
        i = cur_s + 1
        term = (pow2 - (4 * (2 * i - 1)) % MOD) % MOD
        pref.append(pref[-1] * term % MOD)
        pow2 = pow2 * powstep % MOD
        cur_s += 1
    exp_rect = 2 * d * (2 * s - 1)
    rect_factor = pow(2, exp_rect, MOD)
    ans = pref[s] * rect_factor % MOD
    print(ans)