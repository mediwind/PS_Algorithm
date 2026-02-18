import sys
input = sys.stdin.readline

MAX = 300001

parent = list(range(MAX))
dist = [0]*MAX
size = [1]*MAX


def find(x):
    if parent[x] != x:
        root = find(parent[x])
        dist[x] += dist[parent[x]]
        parent[x] = root
    return parent[x]


def move(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    parent[rx] = ry
    dist[rx] = size[ry]
    size[ry] += size[rx]


P = int(input())

for _ in range(P):
    cmd = input().split()
    if cmd[0] == 'M':
        x = int(cmd[1])
        y = int(cmd[2])
        move(x, y)
    else:
        x = int(cmd[1])
        find(x)
        print(str(dist[x]))