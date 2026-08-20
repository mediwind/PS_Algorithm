import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = list(input().strip())
    
    s[0] = s[-1]
    
    print(''.join(s))