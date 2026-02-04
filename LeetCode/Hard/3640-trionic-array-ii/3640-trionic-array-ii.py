class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        inf = -(1 << 50)
        result = a = b = c = inf
        prev = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            na = nb = nc = inf

            if curr > prev:
                na = max(a, prev) + curr
                nc = max(b, c) + curr
            elif curr < prev:
                nb = max(a, b) + curr

            a, b, c = na, nb, nc
            result = max(result, c)
            prev = curr

        return result