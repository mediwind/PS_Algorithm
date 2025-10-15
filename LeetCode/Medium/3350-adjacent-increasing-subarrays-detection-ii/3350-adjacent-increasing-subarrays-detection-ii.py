class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        lo, hi = 1, n // 2
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            ok = False
            limit = n - 2 * mid
            for a in range(limit + 1):
                if inc[a] >= mid and inc[a + mid] >= mid:
                    ok = True
                    break
            if ok:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans