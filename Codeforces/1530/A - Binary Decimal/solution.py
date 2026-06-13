import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n_str = input().rstrip()
    
    ans = max(map(int, n_str))
    
    print(ans)