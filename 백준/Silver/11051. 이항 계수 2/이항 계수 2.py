n, k = map(int, input().split())
dy = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
dy[0][0] = 1

for n in range(1, n + 1):
    for k in range(k + 1):
        if n == k or k == 0:
            dy[n][k] = 1
        else:
            dy[n][k] = (dy[n - 1][k - 1] + dy[n - 1][k]) % 10007

print(dy[n][k])