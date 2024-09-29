import math
from functools import reduce


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


d, m = map(int, input().split())

d_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

v_gcd = reduce(gcd, m_list)
v_lcm = 1

for num in d_list:
    v_lcm = lcm(v_lcm, num)
    if v_lcm > v_gcd or v_lcm == 0:
        print(0)
        exit()

count = 0
i = 1
while i * i < v_gcd:
    if v_gcd % i == 0:
        if i % v_lcm == 0:
            count += 1
        if (v_gcd // i) % v_lcm == 0:
            count += 1
    i += 1

if i * i == v_gcd and i % v_lcm == 0:
    count += 1

print(count)