class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for m in range(n, 0, -1):
                best = 0
                max_take = min(2 * m, n - i)
                for x in range(1, max_take + 1):
                    if x <= m:
                        nm = m 
                    else:
                        nm = x
                    val = suffix[i] - dp[i + x][nm]
                    
                    if val > best:
                        best = val

                dp[i][m] = best

        return dp[0][1]