class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        total = nums[0]

        first, second = 51, 51
        for i in range(1, len(nums)):
            if nums[i] < first:
                second = first
                first = nums[i]
            elif nums[i] < second:
                second = nums[i]
        
        return total + first + second