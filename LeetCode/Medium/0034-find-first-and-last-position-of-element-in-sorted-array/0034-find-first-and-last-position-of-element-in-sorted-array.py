class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
        
    # leftBias = [True/False], if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        lt, rt = 0, len(nums) - 1
        i = -1
        while lt <= rt:
            mid = (lt + rt) // 2
            if target > nums[mid]:
                lt = mid + 1
            elif target < nums[mid]:
                rt = mid - 1
            else:
                i = mid
                if leftBias:
                    rt = mid - 1
                else:
                    lt = mid + 1
        
        return i