class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        NEG = -10**18
        dp = [0, NEG, NEG]
        for x in nums:
            cur = dp[:] 
            for r in range(3):
                if dp[r] != NEG:
                    nxt = dp[r] + x
                    nr = nxt % 3
                    if nxt > cur[nr]:
                        cur[nr] = nxt
            dp = cur
            
        return dp[0]