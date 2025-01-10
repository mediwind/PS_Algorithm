import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = int(math.sqrt(n))
    b = int(math.ceil(n / a))
    perimeter = 2 * (a + b)
    print(perimeter)