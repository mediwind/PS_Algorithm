N, T = map(int, input().split())
subjects = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (T + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    study_time, credit = subjects[i - 1]
    for j in range(T + 1):
        if j < study_time:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - study_time] + credit)

print(dp[N][T])