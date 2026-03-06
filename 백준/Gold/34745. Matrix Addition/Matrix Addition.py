import sys
input = sys.stdin.readline

n, q = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]

diff = [[0]*(n+2) for _ in range(n+2)]

for _ in range(q):
    r1, c1, r2, c2, v = map(int, input().split())

    diff[r1][c1] += v
    diff[r1][c2+1] -= v
    diff[r2+1][c1] -= v
    diff[r2+1][c2+1] += v

for i in range(1, n+1):
    for j in range(1, n+1):
        diff[i][j] += diff[i][j-1]

for j in range(1, n+1):
    for i in range(1, n+1):
        diff[i][j] += diff[i-1][j]

for i in range(n):
    for j in range(n):
        A[i][j] += diff[i+1][j+1]

for row in A:
    print(*row)