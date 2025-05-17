import sys
input = sys.stdin.readline


N, M = map(int, input().split())
K = int(input())
blocked = set()

for _ in range(K):
    a, b, c, d = map(int, input().split())
    blocked.add(((a, b), (c, d)))
    blocked.add(((c, d), (a, b)))

dy = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dy[0][0] = 1

for i in range(N + 1):
    for j in range(M + 1):
        if i > 0:
            if ((i - 1, j), (i, j)) not in blocked:
                dy[i][j] += dy[i - 1][j]
        if j > 0:
            if ((i, j - 1), (i, j)) not in blocked:
                dy[i][j] += dy[i][j - 1]

print(dy[N][M])