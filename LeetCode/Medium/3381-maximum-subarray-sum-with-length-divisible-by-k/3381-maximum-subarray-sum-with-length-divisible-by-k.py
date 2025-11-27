class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minS = [inf for _ in range(k - 1)] + [0]
        prefix, ans= 0, -inf
        for i, x in enumerate(nums):
            prefix += x
            ik = i % k
            ans = max(ans, prefix - minS[ik])
            minS[ik] = min(prefix, minS[ik])

        return ans