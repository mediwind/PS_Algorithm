class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lt, rt = 0, len(nums) - 1

        while lt <= rt:
            mid = (lt + rt) // 2
            # left neighbor greater
            if mid > 0 and nums[mid] < nums[mid - 1]:
                rt = mid - 1
            # right neighbor greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                lt = mid + 1
            else:
                return mid