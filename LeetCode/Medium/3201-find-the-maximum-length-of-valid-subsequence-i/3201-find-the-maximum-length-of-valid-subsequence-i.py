class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        odd_cnt = even_cnt = 0
        for num in nums:
            if num % 2:
                odd_cnt += 1
            else:
                even_cnt += 1
        
        odd_dp = even_dp = 0
        for num in nums:
            if num % 2:
                odd_dp = max(odd_dp, even_dp + 1)
            else:
                even_dp = max(even_dp, odd_dp + 1)
        
        return max(odd_cnt, even_cnt, odd_dp, even_dp)