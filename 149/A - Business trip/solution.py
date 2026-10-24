import sys
input = sys.stdin.readline
 
k = int(input().strip())
a = list(map(int, input().split()))
 
if k == 0:
    print(0)
else:
    a.sort(reverse=True)
    
    total = 0
    months = 0
    
    for growth in a:
        total += growth
        months += 1
        if total >= k:
            break
            
    if total >= k:
        print(months)
    else:
        print(-1)