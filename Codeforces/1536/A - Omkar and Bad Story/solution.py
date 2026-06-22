import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    has_negative = False
    for i in range(n):
        if arr[i] < 0:
            has_negative = True
            break
    
    if has_negative:
        print("NO")
    else:
        print("YES")
        max_val = max(arr)
        
        ans = list(range(max_val + 1))
        
        print(len(ans))
        print(*ans)