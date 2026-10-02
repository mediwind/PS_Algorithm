import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    
    d = 0
    if n % 2 == 0:
        d = 2
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                d = i
                break
        if d == 0:
            d = n
            
    print(n + d + 2 * (k - 1))