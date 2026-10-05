import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    if b >= a:
        print(b)
        continue
        
    if c <= d:
        print(-1)
        continue
        
    rem = a - b
    sleep_per_cycle = c - d
    
    cycles = (rem + sleep_per_cycle - 1) // sleep_per_cycle
    
    print(b + cycles * c)