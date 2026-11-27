import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    m = 1
    while m * 2 <= n - 1:
        m *= 2
        
    ans = []
 
    for i in range(m - 1, -1, -1):
        ans.append(i)
 
    for i in range(m, n):
        ans.append(i)
        
    print(*ans)