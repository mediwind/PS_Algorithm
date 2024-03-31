class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        place = n - 1
        for idx in range(n - 1, -1, -1):
            val = nums[idx]
            if idx + val >= place:
                place = idx
        
        return place == 0