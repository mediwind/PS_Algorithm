N = int(input())
arr = list(map(int, input().split()))
M = int(input())

prefix_sum = [0 for _ in range(N)]
for i in range(N):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]
prefix_sum.insert(0, 0)

dy = [[0 for _ in range(N + 1)] for _ in range(3 + 1)]
for i in range(1, 4):
    for j in range(i * M, N + 1):
        dy[i][j] = max(dy[i][j - 1], dy[i - 1][j - M] + prefix_sum[j] - prefix_sum[j - M])

print(dy[3][N])