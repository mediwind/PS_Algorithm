import math


def max_value(a, b):
    return a if a > b else b


def min_value(a, b):
    return b if a > b else a


def check_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return -1
    return 1


def dfs(a, p, mod):
    if p == 0:
        return 1
    elif p == 1:
        return a
    elif p % 2 == 0:
        half = dfs(a, p // 2, mod)
        return (half * half) % mod
    else:
        return (a * dfs(a, p - 1, mod)) % mod


while True:
    p, a = map(int, input().split())
    if not p and not a:
        break

    p = max_value(a, p)
    a = min_value(a, p)

    mod = p
    if check_prime(p) == 1:
        print("no")
        continue

    if dfs(a, p, mod) == a:
        print("yes")
    else:
        print("no")