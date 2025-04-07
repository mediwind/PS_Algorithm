import math
import sys


def factorize(x):
    """x를 소인수분해하여 {소수: 지수} dict를 반환"""
    factors = dict()
    d = 2
    while d*d <= x:
        while x % d == 0:
            factors[d] = factors.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        factors[x] = factors.get(x, 0) + 1
    return factors


# 검증: LCM(l_ab, c) 가 L이 되어야 함.
def lcm(x, y):
    return x * y // math.gcd(x, y)


a, b, L = map(int, input().split())

# lcm(a, b) = a * b / gcd(a, b)
g = math.gcd(a, b)
l_ab = a // g * b  # a*b//g

# LCM(a, b, c) = LCM(l_ab, c)
# 조건: LCM(l_ab, c) == L 이어야 함.
# 우선 l_ab가 L의 약수가 아니면 불가능.
if L % l_ab != 0:
    print(-1)
    sys.exit(0)

# LCM(l_ab, c) = L가 되려면, L의 소인수분해에 대해 각 소수 p에 대하여
# max(v_p(l_ab), v_p(c)) = v_p(L) 이어야 한다.
# 만약 v_p(l_ab) < v_p(L)라면, c에는 반드시 p^v_p(L) 가 포함되어야 한다.
# v_p(l_ab) == v_p(L)인 소수에 대해서는 c에 p를 포함하지 않아도 된다(최소값을 위해).
# 따라서 최소 c는 각 p에 대해
#   c = ∏_{p: v_p(l_ab) < v_p(L)} p^(v_p(L))

factors_L = factorize(L)
factors_lab = factorize(l_ab)

c = 1
for p, expL in factors_L.items():
    exp_lab = factors_lab.get(p, 0)
    if exp_lab < expL:
        c *= p ** expL

if lcm(l_ab, c) != L:
    print(-1)
else:
    print(c)