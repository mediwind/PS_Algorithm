class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = {0: 1}
        curr_sum = 0
        total_subarrays = 0

        for num in nums:
            curr_sum += num
            if curr_sum - goal in cnt:
                total_subarrays += cnt[curr_sum - goal]
            cnt[curr_sum] = cnt.get(curr_sum, 0) + 1
        
        return total_subarrays