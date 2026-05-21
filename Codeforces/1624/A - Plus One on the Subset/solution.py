import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    
    max_val = max(arr)
    min_val = min(arr)
    
    ans = max_val - min_val
    
    print(ans)