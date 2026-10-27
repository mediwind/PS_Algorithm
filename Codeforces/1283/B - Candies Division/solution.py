import sys
input = sys.stdin.readline
 
t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    
    base = (n // k) * k
    
    rem = n % k
    
    ans = base + min(rem, k // 2)
    
    print(ans)