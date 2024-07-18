class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lt, rt = 0, n - 1

        while lt <= rt:
            mid = (lt + rt) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[lt] <= nums[mid]:
                if target > nums[mid] or target < nums[lt]:
                    lt = mid + 1
                else:
                    rt = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[rt]:
                    rt = mid - 1
                else:
                    lt = mid + 1
    
        return -1