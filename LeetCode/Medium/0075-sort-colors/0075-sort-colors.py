class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointers for the current position of 0, 1, and 2
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[low] and nums[mid], increment low and mid
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Move mid pointer forward
                mid += 1
            else:  # nums[mid] == 2
                # Swap nums[mid] and nums[high], decrement high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1