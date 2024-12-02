import sys
input = sys.stdin.readline


def sieve(n):
    prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False
    return [p for p in range(n + 1) if prime[p]]


primes = sieve(2000000)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = a + b

    if s == 2 or s == 3:
        print("NO")
    elif s % 2 == 0:
        print("YES")
    else:
        s -= 2
        check = False
        for p in primes:
            if p * p > s:
                break
            if s % p == 0:
                print("NO")
                check = True
                break
        if not check:
            print("YES")