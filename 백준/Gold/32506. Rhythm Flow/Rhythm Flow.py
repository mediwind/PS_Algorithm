import sys
input = sys.stdin.readline


def calculate_score(diff):
    if 0 <= diff <= 15:
        return 7
    elif 16 <= diff <= 23:
        return 6
    elif 24 <= diff <= 43:
        return 4
    elif 44 <= diff <= 102:
        return 2
    else:
        return 0


def rhythm_flow(n, m, expected, actual):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score1 = calculate_score(abs(actual[i - 1] - expected[j - 1])) + dp[i - 1][j - 1]
            score2 = dp[i][j - 1]
            score3 = dp[i - 1][j]
            dp[i][j] = max(score1, score2, score3)

    return dp[m][n]


n, m = map(int, input().split())
expected = [int(input().strip()) for _ in range(n)]
actual = [int(input().strip()) for _ in range(m)]

ans = rhythm_flow(n, m, expected, actual)
print(ans)