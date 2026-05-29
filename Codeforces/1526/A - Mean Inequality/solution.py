import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    
    arr.sort()
    
    small_group = arr[:n]
    large_group = arr[n:]
    
    ans = list()
    for i in range(n):
        ans.append(small_group[i])
        ans.append(large_group[i])
    
    print(*ans)