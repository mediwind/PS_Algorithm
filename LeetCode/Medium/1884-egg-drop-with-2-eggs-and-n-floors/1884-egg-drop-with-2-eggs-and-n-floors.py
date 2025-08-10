class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(3)]  # dp[i][j]: i개의 계란, j개의 층
        
        # 계란이 1개인 경우
        for j in range(1, n + 1):
            dp[1][j] = j
        
        # 층이 1개인 경우
        for i in range(1, 3):
            dp[i][1] = 1
        
        # DP 계산
        for i in range(2, 3):  # 계란은 2개
            for j in range(2, n + 1):  # 층 수
                dp[i][j] = float('inf')
                for x in range(1, j + 1):  # x: 계란을 던지는 층
                    # 계란이 깨지는 경우: dp[i-1][x-1] + 1
                    # 계란이 안 깨지는 경우: dp[i][j-x] + 1
                    # 최악의 경우를 최소화
                    dp[i][j] = min(dp[i][j], max(dp[i-1][x-1], dp[i][j-x]) + 1)
        
        return dp[2][n]