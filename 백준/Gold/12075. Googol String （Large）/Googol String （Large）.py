import sys
input = sys.stdin.readline

t = int(input().strip())
for case in range(1, t + 1):
    k = int(input().strip())
    flips = 0
    while True:
        p = 1 << (k.bit_length() - 1)
        if p == k:
            ans = flips & 1
            break
        k = 2 * p - k
        flips += 1
    print(f"Case #{case}: {ans}")