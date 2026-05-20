import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    s = input().rstrip()
    
    sorted_s = sorted(s)
    
    ans = 0
    for i in range(n):
        if s[i] != sorted_s[i]:
            ans += 1
    
    print(ans)