import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())
    
    x_prime = x - 1
    
    row = x_prime % n
    col = x_prime // n
    
    ans_prime = row * m + col
    
    print(ans_prime + 1)