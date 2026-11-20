import sys
import math
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    is_valid = False
    
    if n % 2 == 0:
        half = n // 2
        k = math.isqrt(half)
        if k * k == half:
            is_valid = True
            
    if not is_valid and n % 4 == 0:
        quarter = n // 4
        k = math.isqrt(quarter)
        if k * k == quarter:
            is_valid = True
            
    if is_valid:
        print("YES")
    else:
        print("NO")