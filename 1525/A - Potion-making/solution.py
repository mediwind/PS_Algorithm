import sys
import math
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    k = int(input())
    
    gcd_value = math.gcd(k, 100)
    
    ans = 100 // gcd_value
    
    print(ans)