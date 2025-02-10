from collections import deque

A, K = map(int, input().split())

ch = set()
ch.add(A)
dist = {A: 0}

Q = deque()
Q.append((A, 0))

while Q:
    x, cnt = Q.popleft()
    
    if x == K:
        print(cnt)
        break
    
    if x > K:
        continue
    
    if x + 1 not in ch:
        ch.add(x + 1)
        dist[x + 1] = cnt + 1
        Q.append((x + 1 , cnt + 1))
    
    if x * 2 not in ch:
        ch.add(x * 2)
        dist[x * 2] = cnt + 1
        Q.append((x * 2, cnt + 1))