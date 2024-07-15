class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lt, rt = 0, n - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                lt = mid + 1
            else:
                rt = mid - 1
        
        return lt