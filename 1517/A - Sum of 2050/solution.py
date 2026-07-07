import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n % 2050 != 0:
        print(-1)
    else:
        quotient = n // 2050
        
        ans = 0
        for digit in str(quotient):
            ans += int(digit)
            
        print(ans)