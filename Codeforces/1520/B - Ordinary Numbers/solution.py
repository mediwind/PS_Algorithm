import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    ans = 0
    
    for i in range(1, 10):
        val = i
        while val <= n:
            ans += 1
            val = val * 10 + i
    
    print(ans)