import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    x = input().rstrip()
    ans = (int(x[0]) - 1) * 10
    
    if len(x) == 1:
        ans += 1
    elif len(x) == 2:
        ans += 3
    elif len(x) == 3:
        ans += 6
    else:
        ans += 10
    
    print(ans)