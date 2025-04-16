class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        dp = [0 for _ in range(n + 1)] # dp[i]는 i개의 'A'를 얻기 위한 최소 연산 횟수

        for i in range(2, n + 1):
            dp[i] = i  # 초기값: i개의 'A'를 얻기 위해 i번의 Paste를 수행
            for j in range(1, i // 2 + 1):
                if i % j == 0:  # i가 j로 나누어 떨어지면
                    dp[i] = min(dp[i], dp[j] + (i // j))  # j개의 'A'를 복사 후 Paste

        return dp[n]