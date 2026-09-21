import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    
    if total_sum == 0:
        print("NO")
    else:
        print("YES")
 
        if total_sum > 0:
            a.sort(reverse=True)
        else:
            a.sort()
        print(*a)