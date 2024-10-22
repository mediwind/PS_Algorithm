class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt = 0
        for rt in range(len(nums)):
            if nums[rt]:
                nums[lt], nums[rt] = nums[rt], nums[lt]
                lt += 1
