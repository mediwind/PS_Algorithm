import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    r, b, d = map(int, input().split())
    
    min_val = min(r, b)
    max_val = max(r, b)
    
    if max_val <= min_val * (1 + d):
        print("YES")
    else:
        print("NO")