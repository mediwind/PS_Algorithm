import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mini = min(arr)
    ans = n - arr.count(mini)
    print(ans)