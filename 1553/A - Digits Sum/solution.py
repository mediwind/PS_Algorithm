import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    ans = n // 10
    if str(n)[-1] == '9':
        ans += 1
    print(ans)