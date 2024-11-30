from collections import deque
import sys
input = sys.stdin.readline

n, t, w = map(int, input().split())
Q = deque(tuple(map(int, input().split())) for _ in range(n))
Q

m = int(input())
latter = dict()
for _ in range(m):
    px, tx, cx = map(int, input().split())
    latter[cx] = (px, tx)
latter

second = 0
while second < w:
    order = Q.popleft()
    _id, time = order[0], order[1]
    
    if time > t:
        tmp = list()
        for _ in range(t):
            print(_id)
            second += 1
            if second >= w:
                sys.exit(0)
            if second in latter.keys():
                tmp.append(latter[second])
        Q += tmp
        Q.append((_id, time - t))
    else:
        tmp = list()
        for _ in range(time):
            second += 1
            print(_id)
            if second >= w:
                sys.exit(0)
            if second in latter.keys():
                tmp.append(latter[second])
        Q += tmp