import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n % 7 == 0:
        print(n)
    else:
        base = (n // 10) * 10
        
        for i in range(10):
            if (base + i) % 7 == 0:
                print(base + i)
                break