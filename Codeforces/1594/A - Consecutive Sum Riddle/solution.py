import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    l = -(n - 1)
    r = n
    
    print(l, r)