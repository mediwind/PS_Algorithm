import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    has_non_square = False
    
    for num in arr:
        root = int(num ** 0.5)
        if root * root != num:
            has_non_square = True
            break
            
    if has_non_square:
        print("YES")
    else:
        print("NO")