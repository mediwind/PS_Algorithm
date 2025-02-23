class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = collections.Counter(nums)
        nums = [(val, key) for key, val in nums.items()]
        nums.sort(key = lambda x: -x[0])

        ans = list()
        for i in range(k):
            val, key = nums[i]
            ans.append(key)

        return ans