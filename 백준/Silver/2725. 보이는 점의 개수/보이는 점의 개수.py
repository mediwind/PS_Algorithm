import sys
input = sys.stdin.readline


def compute_gcd(x, y):
    """유클리드 호제법으로 최대공약수 계산"""
    while y > 0:
        x, y = y, x % y
    return x


def precompute_visible_points(limit):
    """0 <= x, y <= limit에서 원점에서 보이는 점의 개수를 미리 계산"""
    dp = [0 for _ in range(limit + 1)]
    dp[1] = 3  # (1, 0), (0, 1), (1, 1)
    for x in range(2, limit + 1):
        count = 0
        for y in range(1, x + 1):
            if compute_gcd(x, y) == 1:
                count += 2  # (x, y)와 (y, x)
        dp[x] = dp[x - 1] + count
    return dp


test_cases = int(input())
max_n = 1000
dp = precompute_visible_points(max_n)

for _ in range(test_cases):
    n = int(input())
    print(dp[n])