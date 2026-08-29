import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    
    left = [a]
    right = [b]
    
    for x in range(n, 0, -1):
        if x == a or x == b:
            continue
            
        if len(left) < n // 2:
            left.append(x)
        else:
            right.append(x)
            
    if min(left) == a and max(right) == b:
        print(*(left + right))
    else:
        print(-1)