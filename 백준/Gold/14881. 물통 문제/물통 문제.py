from math import gcd
import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a, b, c = map(int, input().split())
    # c가 두 물통의 용량 중 더 큰 용량을 초과하면 불가능
    if c > max(a, b):
        print("NO")
        continue
    # c가 a와 b의 최대공약수의 배수이면 측정이 가능
    if c % gcd(a, b) == 0:
        print("YES")
    else:
        print("NO")