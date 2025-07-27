import sys
# input = sys.stdin.readline

MAX_N = 32768

# dp[k][x]: x를 k개의 제곱수 합으로 나타내는 경우의 수
dp = [[0] * MAX_N for _ in range(5)]
dp[0][0] = 1  # 0을 0개의 제곱수로 만드는 경우는 1가지

# 모든 제곱수(1^2 ~ 181^2)
squares = list()
i = 1
while i * i < MAX_N:
    squares.append(i * i)
    i += 1

# DP 채우기 (0-1 배낭 방식, 오름차순 조합)
for sq in squares:
    for k in range(1, 5):
        for x in range(sq, MAX_N):
            dp[k][x] += dp[k - 1][x - sq]

# 입력 및 출력
while True:
    N = int(input())
    if N == 0:
        break
    ans = dp[1][N] + dp[2][N] + dp[3][N] + dp[4][N]
    print(ans)