import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = []
    left = 0
    right = n - 1
    
    while left <= right:
        ans.append(arr[left])
        left += 1
        
        if left <= right:
            ans.append(arr[right])
            right -= 1
            
    print(*ans)