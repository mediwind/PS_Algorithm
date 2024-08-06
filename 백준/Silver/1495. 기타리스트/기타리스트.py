import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
volume = list(map(int, input().split()))

dy = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dy[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dy[i][j] == 1:
            if volume[i] + j <= m:
                dy[i + 1][j + volume[i]] = 1
            if j - volume[i] >= 0:
                dy[i + 1][j - volume[i]] = 1

ans = -1
for i in range(m, - 1, -1):
    if dy[n][i] == 1:
        ans = i
        break

print(ans)