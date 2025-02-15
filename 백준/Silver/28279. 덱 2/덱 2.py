from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
Q = deque()

for _ in range(n):
    order = list(map(int, input().strip().split()))
    
    if order[0] == 1:
        Q.appendleft(order[1])
        
    elif order[0] == 2:
        Q.append(order[1])
        
    elif order[0] == 3:
        if not Q:
            print(-1)
            continue
        
        print(Q.popleft())
        
    elif order[0] == 4:
        if not Q:
            print(-1)
            continue
        
        print(Q.pop())
        
    elif order[0] == 5:
        print(len(Q))
    
    elif order[0] == 6:
        if not Q:
            print(1)
        else:
            print(0)
    
    elif order[0] == 7:
        if not Q:
            print(-1)
            continue
        
        print(Q[0])
    
    else:
        if not Q:
            print(-1)
            continue
        
        print(Q[-1])