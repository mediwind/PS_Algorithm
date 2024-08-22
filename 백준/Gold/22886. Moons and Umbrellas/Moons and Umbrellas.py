import sys
input = sys.stdin.readline


def solve(cj, idx, s, x, y, dp):
    if s[idx] != '?' and (s[idx] == 'C') != (cj == 0):
        return float('inf')
    if dp[cj][idx] != float('inf'):
        return dp[cj][idx]
    if idx + 1 < len(s):
        r1 = solve(cj, idx + 1, s, x, y, dp)
        r2 = solve(1 - cj, idx + 1, s, x, y, dp) + (y if cj else x)
        dp[cj][idx] = min(r1, r2)
    else:
        dp[cj][idx] = 0
    return dp[cj][idx]


t = int(input())
for tc in range(1, t + 1):
    x, y, s = input().split()
    x, y = int(x), int(y)
    dp = [[float('inf')] * len(s) for _ in range(2)]
    res = min(solve(0, 0, s, x, y, dp), solve(1, 0, s, x, y, dp))
    print(f"Case #{tc}: {res}")