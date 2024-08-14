import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
from collections import deque

MAX_N = 100000


def visit(i, k, bb, moonet, C, nbrs):
    moonet[i] = k
    bb[0] = min(bb[0], C[i][0])
    bb[1] = max(bb[1], C[i][0])
    bb[2] = min(bb[2], C[i][1])
    bb[3] = max(bb[3], C[i][1])
    for j in nbrs[i]:
        if moonet[j] == 0:
            visit(j, k, bb, moonet, C, nbrs)


N, M = map(int, input().split())
C = list()
for _ in range(N):
    x, y = map(int, input().split())
    C.append((x, y))

nbrs = [list() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    nbrs[a - 1].append(b - 1)
    nbrs[b - 1].append(a - 1)

moonet = [0 for _ in range(N)]
K = 0
best = 999999999

for i in range(N):
    if moonet[i] == 0:
        bb = [999999999, 0, 999999999, 0]
        visit(i, K + 1, bb, moonet, C, nbrs)
        K += 1
        best = min(best, 2 * (bb[1] - bb[0] + bb[3] - bb[2]))

print(best)