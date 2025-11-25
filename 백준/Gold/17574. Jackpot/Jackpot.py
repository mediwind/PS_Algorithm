def function(m):
    return (1.0 / (N - m)) * (M - (m * K) ** 2)

N, M, K = map(float, input().split())

l, r = 0.0, N - 1.0
for _ in range(100):
    m1 = (l*2 + r) / 3.0
    m2 = (l + r*2) / 3.0
    if function(m1) < function(m2):
        l = m1
    else:
        r = m2

m = (l + r) / 2.0
print(f"{function(m):.6f}")