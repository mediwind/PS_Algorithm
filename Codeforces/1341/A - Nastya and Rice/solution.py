import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    
    min_weight = n * (a - b)
    max_weight = n * (a + b)
    
    if min_weight <= c + d and c - d <= max_weight:
        print("Yes")
    else:
        print("No")