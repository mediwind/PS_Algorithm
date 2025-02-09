from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

Q = deque()
for _ in range(n):
    order = list(input().split())
    
    if order[0] == "push":
        Q.append(order[1])
    elif order[0] == "pop":
        if not Q:
            print(-1)
            continue
        print(Q.popleft())
    elif order[0] == "size":
        print(len(Q))
    elif order[0] == "empty":
        if Q:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if not Q:
            print(-1)
            continue
        print(Q[0])
    elif order[0] == "back":
        if not Q:
            print(-1)
            continue
        print(Q[-1])