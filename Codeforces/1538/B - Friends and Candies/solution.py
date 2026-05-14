import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    
    total = sum(arr)
    
    if total % n:
        print(-1)
    else:
        avg = total // n
        ans = sum(1 for a in arr if a > avg)
        print(ans)