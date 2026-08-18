import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n % 2 == 0:
        print(2, n - 3, 1)
    else:
        k = n - 1
        k //= 2
        
        if k % 2 == 0:
            print(k - 1, k + 1, 1)
        else:
            print(k - 2, k + 2, 1)