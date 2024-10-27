class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lt = 0
        n = len(nums)
        ans = 0
        zero_cnt = 0
        for rt in range(n):
            if nums[rt] == 0:
                zero_cnt += 1
            
            while zero_cnt > k:
                if nums[lt] == 0:
                    zero_cnt -= 1
                lt += 1
            
            ans = max(ans, rt - lt + 1)
        
        return ans