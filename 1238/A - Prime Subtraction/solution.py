import sys
input = sys.stdin.readline
 
t = int(input().strip())
 
for _ in range(t):
    x, y = map(int, input().split())
    
    if x - y > 1:
        print("YES")
    else:
        print("NO")