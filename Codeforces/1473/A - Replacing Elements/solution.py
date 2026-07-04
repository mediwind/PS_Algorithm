import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    
    already_ok = True
    for num in arr:
        if num > d:
            already_ok = False
            break
            
    if already_ok:
        print("YES")
        continue
        
    arr.sort()
    
    if arr[0] + arr[1] <= d:
        print("YES")
    else:
        print("NO")