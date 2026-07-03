import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().strip()
    
    if s.count('N') == 1:
        print("NO")
    else:
        print("YES")