import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n % 3 == 0:
        print(n // 3, 0, 0)
    elif n % 3 == 1:
        if n >= 7:
            print((n - 7) // 3, 0, 1)
        else:
            print(-1)
    else:
        if n >= 5:
            print((n - 5) // 3, 1, 0)
        else:
            print(-1)