class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        
        NEG = float('-inf')
        
        dp = [[[NEG]*3 for _ in range(n)] for _ in range(m)]
        
        v = coins[0][0]

        if v >= 0:
            for k in range(3):
                dp[0][0][k] = v
        else:
            dp[0][0][0] = v
            dp[0][0][1] = 0
            dp[0][0][2] = 0
        
        for i in range(m):
            for j in range(n):
                
                if i == 0 and j == 0:
                    continue
                
                v = coins[i][j]
                
                for k in range(3):
                    
                    best = NEG
                    
                    if i > 0:
                        best = max(best, dp[i-1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j-1][k])
                    
                    if best != NEG:
                        dp[i][j][k] = max(dp[i][j][k], best + v)
                    
                    if v < 0 and k > 0:
                        prev = NEG
                        if i > 0:
                            prev = max(prev, dp[i-1][j][k-1])
                        if j > 0:
                            prev = max(prev, dp[i][j-1][k-1])
                        
                        if prev != NEG:
                            dp[i][j][k] = max(dp[i][j][k], prev)
        
        return max(dp[m-1][n-1])