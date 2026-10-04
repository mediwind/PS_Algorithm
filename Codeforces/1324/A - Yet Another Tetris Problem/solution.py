import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    base_parity = a[0] % 2
    possible = True
    
    for val in a:
        if val % 2 != base_parity:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")