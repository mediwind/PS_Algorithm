import sys
from collections import Counter
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    s = input().rstrip()
    
    cnt = Counter(s)
    
    ans = sum(min(v, 2) for v in cnt.values()) // 2
    print(ans)