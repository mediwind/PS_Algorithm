from math import gcd
import sys

n, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ones = [A[i] for i in range(n) if B[i] == 1]
zeros = [A[i] for i in range(n) if B[i] == 0]

if not ones:
    if any(z == 1 for z in zeros):
        print(-1)
    else:
        print(1 if L >= 1 else -1)
else:
    l = 1
    for v in ones:
        l = l * v // gcd(l, v)
        if l > L:
            print(-1)
            sys.exit(0)
    for z in zeros:
        if l % z == 0:
            print(-1)
            sys.exit(0)
    print(l)