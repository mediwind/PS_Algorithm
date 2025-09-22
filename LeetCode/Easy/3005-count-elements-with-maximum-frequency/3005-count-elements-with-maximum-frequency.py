class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        maxi = max(counts.values())
        
        ans = 0
        for num in set(nums):
            if counts[num] == maxi:
                ans += counts[num]

        return ans