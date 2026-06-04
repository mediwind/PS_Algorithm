from collections import Counter
import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(lambda x: abs(int(x)), input().split()))
    cnt = Counter(arr)
 
    ans = 0
    for key, value in cnt.items():
        if key == 0:
            ans += 1
        elif value == 1:
            ans += 1
        elif value >= 2:
            ans += 2
 
    print(ans)