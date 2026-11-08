import sys
input = sys.stdin.readline
 
n = int(input().strip())
a = list(map(int, input().split()))
 
a.sort()
 
ans = min(a[n - 2] - a[0], a[n - 1] - a[1])
 
print(ans)