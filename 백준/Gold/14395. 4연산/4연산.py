from collections import deque

s, t = map(int, input().split())
Q = deque()
ch = set()

if s == t:
    print(0)
elif t == 1:
    print('/')
else:
    Q.append((s, ''))
    ch.add(s)
    while Q:
        x, o = Q.popleft()
        if x == t:
            print(o)
            break
        
        if x**2 <= 10**9 and x**2 not in ch:
            ch.add(x**2)
            Q.append((x**2, o + '*'))
        if x*2 <= 10**9 and x*2 not in ch:
            ch.add(x*2)
            Q.append((x*2, o + '+'))
        if x//x not in ch:
            ch.add(x//x)
            Q.append((x//x, o + '/'))
    else:
        print(-1)