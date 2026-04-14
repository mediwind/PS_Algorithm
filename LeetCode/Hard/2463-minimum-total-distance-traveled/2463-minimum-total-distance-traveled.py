class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        INF = float('inf')
        
        # dp[i][j]: i개의 로봇, j개의 factory 고려
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        
        # 로봇 0개는 항상 0
        for j in range(m + 1):
            dp[0][j] = 0
        
        # DP 진행
        for j in range(1, m + 1):
            factory_pos, limit = factory[j - 1]
            
            for i in range(n + 1):
                # 1. 현재 factory 사용 안함
                dp[i][j] = dp[i][j - 1]
                
                # 2. 현재 factory에 k개 할당
                cost = 0
                for k in range(1, min(limit, i) + 1):
                    cost += abs(robot[i - k] - factory_pos)
                    
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - k][j - 1] + cost
                    )
        
        return dp[n][m]