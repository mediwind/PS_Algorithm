import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input().rstrip())
    number = list(input().rstrip())
    ans = int(number[-1])
    
    for i in range(n - 1):
        if number[i] != '0':
            ans += (int(number[i]) + 1)
    
    print(ans)