class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        lt, rt = 0, len(nums) - 1

        while lt <= rt:
            if nums[lt] < nums[rt]:
                res = min(res, nums[lt])
                break

            mid = (lt + rt) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[lt]:
                lt = mid + 1
            else:
                rt = mid - 1
        
        return res