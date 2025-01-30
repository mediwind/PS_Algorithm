class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        lt, rt = 0, n - 1
        while lt < rt:
            mid = (lt + rt) // 2
            
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] != nums[mid + 1]:
                rt = mid
            else:
                lt = mid + 2
        
        return nums[lt]
