class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = list()
        for num in nums:
            if num & 1:
                ans.append(num & ~(((num + 1) & ~num) >> 1))
            else:
                ans.append(-1)
        
        return ans