import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    q = n // 2020
    r = n % 2020
    
    if r <= q:
        print("YES")
    else:
        print("NO")