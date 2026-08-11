import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n < 6:
        print(15)
    else:
        if n % 2 != 0:
            n += 1
            
        print((n // 2) * 5)