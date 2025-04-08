from collections import deque
import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    Q = deque()
    Q.append(1)

    while Q:
        num = Q.popleft()
        if num % N == 0:
            print(num)
            break
        else:
            Q.append(num * 10)
            Q.append(num * 10 + 1)