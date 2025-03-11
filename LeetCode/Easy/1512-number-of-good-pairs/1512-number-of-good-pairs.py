class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = dict()
        ans = 0

        for i in range(len(nums)):
            if nums[i] in pairs:
                ans += pairs[nums[i]]
            
            pairs[nums[i]] = pairs.get(nums[i], 0) + 1
        
        return ans