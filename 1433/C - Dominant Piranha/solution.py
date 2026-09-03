import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_val = max(arr)
    ans = -1
    
    for i in range(n):
        if arr[i] == max_val:
            if i > 0 and arr[i - 1] < max_val:
                ans = i + 1
                break
            if i < n - 1 and arr[i + 1] < max_val:
                ans = i + 1
                break
                
    print(ans)