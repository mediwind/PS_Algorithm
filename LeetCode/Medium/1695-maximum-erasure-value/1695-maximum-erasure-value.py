class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        lt = rt = 0
        curr_sum = 0
        ans = 0

        while rt < n:
            if nums[rt] not in s:
                s.add(nums[rt])
                curr_sum += nums[rt]
                rt += 1
                ans = max(ans, curr_sum)
            else:
                s.discard(nums[lt])
                curr_sum -= nums[lt]
                lt += 1
        
        return ans