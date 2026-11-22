import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    min_val = min(arr)
    target = n // 2
    cnt = 0
    
    for x in arr:
        if x == min_val:
            continue
        
        print(x, min_val)
        cnt += 1
        if cnt == target:
            break