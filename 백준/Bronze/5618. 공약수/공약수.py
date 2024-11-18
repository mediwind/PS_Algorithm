import math


def gcd_multiple(numbers):
    gcd_value = numbers[0]
    for num in numbers[1:]:
        gcd_value = math.gcd(gcd_value, num)
    return gcd_value


n = int(input())
arr = list(map(int, input().split()))

gcd_value = gcd_multiple(arr)

for i in range(1, gcd_value + 1):
    if gcd_value % i == 0:
        print(i)