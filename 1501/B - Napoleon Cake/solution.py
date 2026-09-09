import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = []
    cream = 0
    
    for i in range(n - 1, -1, -1):
        cream = max(cream, a[i])
        
        if cream > 0:
            ans.append(1)
            cream -= 1
        else:
            ans.append(0)
            
    ans.reverse()
    print(*ans)