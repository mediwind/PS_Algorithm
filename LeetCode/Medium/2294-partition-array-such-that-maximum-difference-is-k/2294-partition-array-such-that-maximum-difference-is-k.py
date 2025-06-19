class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        cnt = 1
        start = nums[0]
        for num in nums:
            if num - start > k:
                cnt += 1
                start = num
        
        return cnt