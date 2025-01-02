class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        increasing = False
        decreasing = False

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                increasing = True
            if nums[i - 1] < nums[i]:
                decreasing = True
            
            if increasing and decreasing:
                return False
        
        return True