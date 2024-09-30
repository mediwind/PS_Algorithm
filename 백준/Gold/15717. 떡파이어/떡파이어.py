def mod_exp(base, exponent, modulus):
    result = 1
    while exponent:
        if exponent % 2:
            result = result * base % modulus
        base = base * base % modulus
        exponent //= 2
    return result


n = int(input())
if n == 0:
    print(1)
else:
    print(mod_exp(2, n - 1, 1000000007))