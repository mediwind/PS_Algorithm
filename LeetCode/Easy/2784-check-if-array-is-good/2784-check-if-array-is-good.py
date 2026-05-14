class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        return sorted(nums) == [i for i in range(1, n + 1)] + [n]