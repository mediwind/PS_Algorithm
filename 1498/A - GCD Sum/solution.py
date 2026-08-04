from math import gcd
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    while True:
        digit_sum = 0
        for c in str(n):
            digit_sum += int(c)
        
        if gcd(n, digit_sum) > 1:
            print(n)
            break
        
        n += 1