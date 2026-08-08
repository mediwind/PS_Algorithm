import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    if a == b:
        print(0, 0)
        continue
    
    g = abs(a - b)
    
    r = a % g
    
    min_ops = min(r, g - r)
    
    print(g, min_ops)