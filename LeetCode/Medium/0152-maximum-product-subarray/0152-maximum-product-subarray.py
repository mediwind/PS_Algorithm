class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_prod = max_prod = ans = nums[0]

        for num in nums[1:]:
            candidates = (num, min_prod * num, max_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)
            ans = max(ans, max_prod)
        
        return ans