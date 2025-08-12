class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        # 가능한 제곱수 리스트
        powers = list()
        i = 1
        while i ** x <= n:
            powers.append(i ** x)
            i += 1

        # dp[j]: 합이 j가 되는 경우의 수
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for p in powers:
            for j in range(n, p - 1, -1):
                dp[j] = (dp[j] + dp[j - p]) % MOD
        
        return dp[n]