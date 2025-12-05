class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        cnt = 0

        for i in range(n - 1):
            left_sum += nums[i]
            right_sum = total - left_sum

            if (left_sum % 2) == (right_sum % 2):
                cnt += 1
        
        return cnt