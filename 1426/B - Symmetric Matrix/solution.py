import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    has_symmetric_tile = False
    
    for _ in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if b == c:
            has_symmetric_tile = True
            
    if m % 2 == 0 and has_symmetric_tile:
        print("YES")
    else:
        print("NO")