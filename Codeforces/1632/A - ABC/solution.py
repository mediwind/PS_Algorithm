import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().rstrip()
    
    if n == 1:
        print("YES")
    elif n == 2 and len(set(s)) == n:
        print("YES")
    else:
        print("NO")