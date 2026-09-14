import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    possible = True
    for i in range(n):
        diff = b[i] - a[i]
        if diff != 0 and diff != 1:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")