import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    total = sum(arr)
    q, r = total // n, total % n
 
    ans = r * (n - r)
    print(ans)