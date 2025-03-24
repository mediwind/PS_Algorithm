import math

n = int(input())

sqrt_n = int(math.sqrt(n) + (10 ** -7))
total_sum = 0

for divisor in range(2, sqrt_n + 1):
    quotient = n // divisor
    total_sum += divisor * (quotient - divisor + 1)
    total_sum += (quotient - divisor) * (quotient + divisor + 1) // 2
    total_sum %= 1_000_000

print(total_sum)