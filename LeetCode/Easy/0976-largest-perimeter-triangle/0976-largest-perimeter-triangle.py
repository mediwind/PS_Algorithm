class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums, reverse = True)
        
        for i in range(n - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c and b < a + c and c < a + b:
                return a + b + c
        
        return 0