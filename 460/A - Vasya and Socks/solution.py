import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
 
ans = n + (n - 1) // (m - 1)
 
print(ans)