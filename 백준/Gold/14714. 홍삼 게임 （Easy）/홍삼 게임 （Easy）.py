from collections import deque
import sys


def wrap(pos, d, N):
    return ((pos - 1 + d) % N) + 1


N, A ,B ,DA, DB = map(int, input().split())
vis = [[[False] * 2 for _ in range(N + 1)] for __ in range(N + 1)]
q = deque()
q.append((A, B, 0, 0))
vis[A][B][0] = True
while q:
    a, b, turn, steps = q.popleft()
    if turn == 0:
        for d in (DA, -DA):
            na = wrap(a, d, N)
            if na == b:
                print(steps + 1)
                sys.exit(0)
            if not vis[na][b][1]:
                vis[na][b][1] = True
                q.append((na, b, 1, steps + 1))
    else:
        for d in (DB, -DB):
            nb = wrap(b, d, N)
            if nb == a:
                print(steps + 1)
                sys.exit(0)
            if not vis[a][nb][0]:
                vis[a][nb][0] = True
                q.append((a, nb, 0, steps + 1))

print("Evil Galazy")