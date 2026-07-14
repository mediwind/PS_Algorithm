import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if sum(arr) == x:
        print("NO")
        continue
        
    print("YES")
    curr_sum = 0
    
    for i in range(n):
        if curr_sum + arr[i] == x:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
        curr_sum += arr[i]
        
    print(*arr)