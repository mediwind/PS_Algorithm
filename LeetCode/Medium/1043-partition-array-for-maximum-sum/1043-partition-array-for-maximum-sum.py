class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            m = 0
            for j in range(1, min(k, i) + 1):
                m = max(m, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + m * j)
        
        return dp[n]