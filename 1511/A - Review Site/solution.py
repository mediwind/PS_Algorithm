from collections import Counter
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    cnt = Counter(arr)
    ans = cnt[1] + cnt[3]
    print(ans)