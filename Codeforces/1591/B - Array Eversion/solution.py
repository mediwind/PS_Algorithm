import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    cur_max = arr[-1]
    ans = 0
    
    for i in range(n - 2, -1, -1):
        if arr[i] > cur_max:
            cur_max = arr[i]
            ans += 1
            
    print(ans)