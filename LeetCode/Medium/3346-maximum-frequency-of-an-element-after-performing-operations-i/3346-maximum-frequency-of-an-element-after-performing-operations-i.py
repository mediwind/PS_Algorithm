class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mn = min(nums) - k
        mx = max(nums) + k

        offset = -mn
        size = mx - mn + 1
        diff = [0] * (size + 1)
        equals = [0] * size
        for v in nums:
            L = v - k + offset
            R = v + k + offset
            diff[L] += 1
            diff[R + 1] -= 1
            equals[v + offset] += 1

        cur = 0
        best = 0
        for i in range(size):
            cur += diff[i]
            eq = equals[i]
            conv = cur - eq
            
            if conv < 0:
                conv = 0
            val = eq + min(numOperations, conv)

            if val > best:
                best = val

        return best