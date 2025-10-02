class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ones = sum(x & 1 for x in nums)
        return [0] * (len(nums) - ones) + [1] * ones