import heapq as hq
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    pa = find(a)
    pb = find(b)
    
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


p, w = map(int, input().split())
c, v = map(int, input().split())

Q = list()
for _ in range(w):
    st, ed, wd = map(int, input().split())
    hq.heappush(Q, (-wd, st, ed))

parent = list(range(p + 1))
while Q:
    wd, st, ed = hq.heappop(Q)
    wd = -wd
    union(st, ed)
    
    if find(c) == find(v):
        print(wd)
        break