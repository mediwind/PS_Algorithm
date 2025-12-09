class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import Counter

        MOD = 10**9 + 7
        right = Counter(nums)
        left = Counter()
        ans = 0
        for x in nums:
            right[x] -= 1
            t = 2 * x
            ans = (ans + left[t] * right[t]) % MOD
            left[x] += 1
            
        return ans