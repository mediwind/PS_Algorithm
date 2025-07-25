class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = float('-inf')
        positiveNums = set([num for num in nums if num > 0])
        
        return max(nums) if len(positiveNums) == 0 else sum(positiveNums)