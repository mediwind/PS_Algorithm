import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().rstrip()
    ans = "".join(sorted(s))
    
    print(ans)