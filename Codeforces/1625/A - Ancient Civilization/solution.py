import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))
    
    y = 0
    for j in range(l):
        cnt1 = 0
        for x in arr:
            if (x >> j) & 1:
                cnt1 += 1
                
        cnt0 = n - cnt1
        
        if cnt1 > cnt0:
            y |= (1 << j)
            
    print(y)