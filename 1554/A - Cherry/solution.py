import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    
    ans = 0
    for i in range(n - 1):
        ans = max(ans, arr[i] * arr[i + 1])
        
    print(ans)