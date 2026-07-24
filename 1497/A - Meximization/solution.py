from collections import Counter
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    cnt = Counter(arr)
    head, tail = list(), list()
    for key, val in cnt.items():
        if val > 1:
            tail.extend([key] * (val - 1))
        
        head.append(key)
    
    ans = head + tail
    print(*ans)