import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    x0, n = map(int, input().split())
    
    rem = n % 4
    
    if rem == 0:
        d = 0
    elif rem == 1:
        d = -n
    elif rem == 2:
        d = 1
    else:
        d = n + 1
    
    if x0 % 2 != 0:
        d = -d
    
    print(x0 + d)