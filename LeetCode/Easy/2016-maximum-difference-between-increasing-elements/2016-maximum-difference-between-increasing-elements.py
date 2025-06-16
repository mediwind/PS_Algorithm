class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        mini = nums[0]
        ans = float('-inf')

        for i in range(1, n):
            mini = min(mini, nums[i])
            if nums[i] > mini:
                ans = max(ans, nums[i] - mini)
        
        if ans == float('-inf'):
            return -1
        return ans