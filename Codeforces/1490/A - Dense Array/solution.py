import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    
    for i in range(n - 1):
        mini = min(arr[i], arr[i + 1])
        maxi = max(arr[i], arr[i + 1])
        
        while mini * 2 < maxi:
            mini *= 2
            ans += 1
            
    print(ans)