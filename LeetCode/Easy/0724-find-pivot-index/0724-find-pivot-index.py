class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        to_left = [0 for _ in range(n)]
        to_left[0] = nums[0]
        for i in range(1, n):
            to_left[i] = nums[i] + to_left[i - 1]
        
        to_right = [0 for _ in range(n)]
        to_right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            to_right[i] = nums[i] + to_right[i + 1]
        
        for i in range(n):
            if to_left[i] == to_right[i]:
                return i
        
        return -1