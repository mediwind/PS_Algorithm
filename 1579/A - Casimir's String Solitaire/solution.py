from collections import Counter
import sys
input = sys.stdin.readline
 
t = int(input().rstrip())
for _ in range(t):
    s = input().rstrip()
    cnt = Counter(s)
    
    if cnt['A'] + cnt['C'] != cnt['B']:
        print("NO")
    else:
        print("YES")