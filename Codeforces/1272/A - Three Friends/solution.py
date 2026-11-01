import sys
input = sys.stdin.readline
 
q = int(input().strip())
for _ in range(q):
    a, b, c = map(int, input().split())
    
    diff = max(a, b, c) - min(a, b, c)
    
    ans = max(0, 2 * (diff - 2))
    print(ans)