n, k = map(int, input().split())

pairs = 1 << (n - k - 1)
val = 0

for i in range(1 << k):
    for j in range(pairs):
        print(val, (1 << n) - 1 - val)
        val += 1