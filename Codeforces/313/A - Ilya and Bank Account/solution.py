import sys
input = sys.stdin.readline
 
n = int(input())
 
if n >= 0:
    print(n)
else:
    s = str(n)
    opt1 = int(s[:-1])
    opt2 = int(s[:-2] + s[-1])
    
    print(max(opt1, opt2))