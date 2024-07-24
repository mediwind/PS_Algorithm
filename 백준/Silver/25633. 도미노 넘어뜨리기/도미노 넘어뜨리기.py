N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i, 0, -1):
        if dp[j - 1] == 0:
            continue
        if dp[j - 1] >= arr[i]:
            dp[j] = max(dp[j], dp[j - 1] + arr[i])
    dp[1] = max(dp[1], arr[i])

for i in range(N, 0, -1):
    if dp[i]:
        print(i)
        break