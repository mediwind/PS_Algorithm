import sys
from collections import Counter
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    
    cnt = dict()
    for char in string:
        if char not in cnt:
            cnt[char] = 1
        else:
            if cnt[char] < 2:
                cnt[char] += 1
    
    ans = 0
    res = 0
    for val in cnt.values():
        if val == 2:
            ans += 1
        else:
            res += 1
    
    ans += res // 2
    print(ans)