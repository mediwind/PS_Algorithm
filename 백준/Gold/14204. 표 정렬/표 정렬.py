import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

row_group = []

for i in range(N):
    groups = set()
    for j in range(M):
        v = table[i][j]
        groups.add((v - 1) // M)
    if len(groups) != 1:
        print(0)
        sys.exit(0)
    row_group.append(groups.pop())

if set(row_group) != set(range(N)):
    print(0)
    sys.exit(0)

col_group = []

for j in range(M):
    groups = set()
    for i in range(N):
        v = table[i][j]
        groups.add((v - 1) % M)
    if len(groups) != 1:
        print(0)
        sys.exit(0)
    col_group.append(groups.pop())

if set(col_group) != set(range(M)):
    print(0)
else:
    print(1)