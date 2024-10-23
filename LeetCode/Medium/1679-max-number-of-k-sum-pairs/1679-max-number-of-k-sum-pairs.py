class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        lt = 0
        rt = n - 1
        cnt = 0
        while lt < rt:
            tmp = nums[lt] + nums[rt]
            if tmp > k:
                rt -= 1
            elif tmp < k:
                lt += 1
            else:
                cnt += 1
                lt += 1
                rt -= 1
        
        return cnt