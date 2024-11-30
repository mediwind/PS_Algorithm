from collections import deque
import sys
input = sys.stdin.readline

n, t, w = map(int, input().split())
Q = deque(tuple(map(int, input().split())) for _ in range(n))

m = int(input())
latter = dict()
for _ in range(m):
    px, tx, cx = map(int, input().split())
    latter[cx] = (px, tx)

second = 0
while second < w:
    order = Q.popleft()
    _id, time = order[0], order[1]
    
    tmp = list()
    for _ in range(min(time, t)):
        print(_id)
        second += 1
        if second >= w:
            sys.exit(0)
        if second in latter.keys():
            tmp.append(latter[second])
    Q += tmp
    if time > t:
        Q.append((_id, time - t))