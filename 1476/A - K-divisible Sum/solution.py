import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    s = ((n + k - 1) // k) * k
    ans = (s + n - 1) // n
    print(ans)