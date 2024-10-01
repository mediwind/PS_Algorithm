import math

MAX = 100000


def factorize(x, prime_factors):
    limit = int(math.sqrt(x))
    for i in range(2, limit + 1):
        while x % i == 0:
            x //= i
            prime_factors[i] += 1
    if x > 1:
        prime_factors[x] += 1


def defactorize(x, prime_factors):
    limit = int(math.sqrt(x))
    for i in range(2, limit + 1):
        while x % i == 0:
            x //= i
            prime_factors[i] -= 1
    if x > 1:
        prime_factors[x] -= 1


n = int(input())
expression = input().split()

prime_factors = [0] * (MAX + 1)
zero_present = False
negative_factors = False

num = int(expression[0])
if num < 0:
    num = abs(num)
elif num == 0:
    zero_present = True
if num:
    factorize(num, prime_factors)

for i in range(1, len(expression), 2):
    operator = expression[i]
    num = int(expression[i + 1])
    if num < 0:
        num = abs(num)
    elif num == 0:
        zero_present = True
    if operator == '/':
        defactorize(num, prime_factors)
    elif num:
        factorize(num, prime_factors)

if zero_present:
    print("mint chocolate")
else:
    for i in range(2, MAX + 1):
        if prime_factors[i] < 0:
            negative_factors = True
            break
    if negative_factors:
        print("toothpaste")
    else:
        print("mint chocolate")