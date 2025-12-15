n, c = map(int, input().split())

dy = [[0] * n for _ in range(n)]

for i in range(n):
    dy[i][i] = i + 1

for i in reversed(range(n)):
    for j in range(i + 1, n):
        dy[i][j] = min(
            max(
                dy[k + 1][j] + c if k < j else -1,
                dy[i][k - 1] + k + 1,
                dy[k][k],
            )
            for k in range(i, j + 1)
        )

print(dy[0][-1])