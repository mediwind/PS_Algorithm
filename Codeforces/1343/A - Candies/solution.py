import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    k = 2
    while True:
        val = (1 << k) - 1
        
        if n % val == 0:
            print(n // val)
            break
            
        k += 1