import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().rstrip()
    
    c0 = s.count('0')
    c1 = s.count('1')
    
    if c0 != c1:
        print(min(c0, c1))
    else:
        print(c0 - 1)