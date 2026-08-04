class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = set(nums)
        mini, maxi = min(nums), max(nums)

        ans = list()
        for i in range(mini, maxi):
            if i not in nums:
                ans.append(i)

        return ans