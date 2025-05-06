import math

x, y = map(int, input().split())

gcd = math.gcd(x, y)

result = x + y - gcd
print(result)