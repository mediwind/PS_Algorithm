import sys
input = sys.stdin.readline

data = input().split()

N = int(data[0])
K = int(data[1])
data = list()
for _ in range(N):
    tmp = list(map(int, input().split()))
    data += tmp

arr = [[0] * (2 * N - 1) for _ in range(2 * N - 1)]
pSum = [[0] * (2 * N) for _ in range(2 * N)]

index = 0
for i in range(N):
    for j in range(N):
        arr[i + j][N - 1 - i + j] = int(data[index])
        index += 1

for i in range(2 * N - 1):
    for j in range(2 * N - 1):
        pSum[i + 1][j + 1] = pSum[i + 1][j] + pSum[i][j + 1] - pSum[i][j] + arr[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        y = i + j
        x = N - 1 - i + j
        sy = max(y - K, 0)
        sx = max(x - K, 0)
        ey = min(y + K, 2 * (N - 1))
        ex = min(x + K, 2 * (N - 1))
        sum_val = pSum[ey + 1][ex + 1] - pSum[ey + 1][sx] - pSum[sy][ex + 1] + pSum[sy][sx]
        ans = max(ans, sum_val)

print(ans)