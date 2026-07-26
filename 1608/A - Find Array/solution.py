import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    ans = list(range(2, n + 2))
    
    print(*ans)