class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - 1 - i]
            ans = max(ans, pair_sum)
        
        return ans