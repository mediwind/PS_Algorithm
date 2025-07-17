import sys
# input = sys.stdin.readline


def multiply(m1, m2):
    ans = [0.0] * 4
    ans[0] = m1[0] * m2[0] + m1[1] * m2[2]
    ans[1] = m1[0] * m2[1] + m1[1] * m2[3]
    ans[2] = m1[2] * m2[0] + m1[3] * m2[2]
    ans[3] = m1[2] * m2[1] + m1[3] * m2[3]
    for i in range(4):
        m1[i] = ans[i]


T = int(input().rstrip())
for ca in range(1, T + 1):
    n, x, k, a, b, c = map(float, input().rstrip().split())
    n = int(n)
    x = int(x)
    k = int(k)
    a /= 100
    b /= 100
    c /= 100

    ans0 = [1.0, 0.0, 0.0, 1.0]
    ans1 = [1.0, 0.0, 0.0, 1.0]
    cur0 = [1.0, a, 0.0, b + c]
    cur1 = [a, c, b + c, a + b]

    nn = n
    while nn:
        if nn & 1:
            multiply(ans0, cur0)
            multiply(ans1, cur1)
        multiply(cur0, cur0)
        multiply(cur1, cur1)
        nn >>= 1

    base = 1
    res = 0.0
    xx, kk = x, k
    while xx or kk:
        p1 = 1.0 if xx & 1 else 0.0
        p0 = 1.0 - p1
        if kk & 1:
            c0 = ans1[2]
            c1 = ans1[3]
        else:
            c0 = ans0[2]
            c1 = ans0[3]
        res += (c0 * p0 + c1 * p1) * base
        base <<= 1
        xx >>= 1
        kk >>= 1

    print(f"Case #{ca}: {res:.10f}")