class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums = nums + nums[:1]

        ans = float('-inf')
        for i in range(1, len(nums)):
            ans = max(ans, abs(nums[i] - nums[i - 1]))
        
        return ans
