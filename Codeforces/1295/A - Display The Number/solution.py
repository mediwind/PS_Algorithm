import sys
input = sys.stdin.readline
 
t = int(input().strip())
 
for _ in range(t):
    n = int(input().strip())
    
    if n % 2 == 0:
        print("1" * (n // 2))
    else:
        print("7" + "1" * ((n - 3) // 2))