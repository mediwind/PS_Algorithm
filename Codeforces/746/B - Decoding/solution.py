import sys
from collections import deque
input = sys.stdin.readline
 
n = int(input().strip())
s = input().strip()
 
dq = deque()
 
for i in range(n):
    rem = n - i
    if rem % 2 == 1:
        dq.append(s[i])
    else:
        dq.appendleft(s[i])
 
print("".join(dq))