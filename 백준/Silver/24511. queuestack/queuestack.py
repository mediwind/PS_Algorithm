import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
data_structure = list(map(int, input().split()))
element = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

Q = deque()
for ds, el in zip(data_structure, element):
    if ds == 0:
        Q.appendleft(el)

if not Q:
    print(*arr)
    sys.exit(0)

for m in arr:
    Q.append(m)
    print(Q.popleft(), end = " ")