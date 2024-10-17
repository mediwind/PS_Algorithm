from math import factorial


def calculate_combination(n, k):
    comb = factorial(n) // (factorial(n - k) * factorial(k))
    return comb


n, k = map(int, input().split())
arr = list(map(int, input().split()))

comb = calculate_combination(n, k)
result = (comb * 2 ** (k - 1)) % (10 ** 9 + 7)
print(result)