import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    
    while x > 20 and n > 0:
        x = x // 2 + 10
        n -= 1
        
    if x <= m * 10:
        print("YES")
    else:
        print("NO")