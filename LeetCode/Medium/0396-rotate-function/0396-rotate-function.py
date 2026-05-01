class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        ans = 0
        for idx, val in enumerate(nums):
            ans += idx * val
        F = ans
        
        for i in range(1, n):
            F += (total - (n * nums[n - i]))
            ans = max(ans, F)
        
        return ans