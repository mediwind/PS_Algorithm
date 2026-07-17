from collections import deque
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = deque(list(range(1, n + 1)))
    arr.rotate(1)
    print(*arr)