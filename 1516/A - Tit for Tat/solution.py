import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(n - 1):
        if k == 0:
            break
            
        take = min(arr[i], k)
        
        arr[i] -= take
        arr[n - 1] += take
        k -= take
        
    print(*arr)