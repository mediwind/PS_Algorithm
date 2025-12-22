import sys
input = sys.stdin.readline

parent = []
size = []

def dsu_init(n):
    global parent, size
    parent = list(range(n))
    size = [1] * n

def dsu_find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def dsu_union(a, b):
    ra = dsu_find(a)
    rb = dsu_find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

def read_nonempty_line():
    while True:
        line = input()
        if line.strip():
            return line

t = int(read_nonempty_line())
for _ in range(t):
    n = int(read_nonempty_line())

    constraints = []
    vals = []

    for _ in range(n):
        parts = read_nonempty_line().split()
        i, j, e = map(int, parts)
        constraints.append((i, j, e))
        vals.append(i)
        vals.append(j)

    vals = sorted(set(vals))
    idx = {v: i for i, v in enumerate(vals)}

    dsu_init(len(vals))

    for i, j, e in constraints:
        if e == 1:
            dsu_union(idx[i], idx[j])

    ok = True
    for i, j, e in constraints:
        if e == 0 and dsu_find(idx[i]) == dsu_find(idx[j]):
            ok = False
            break

    print("YES" if ok else "NO")