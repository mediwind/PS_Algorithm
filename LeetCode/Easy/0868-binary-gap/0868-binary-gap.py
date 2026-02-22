class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        ans = 0
        pos = 0

        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, pos - last)
                last = pos
            pos += 1
            n >>= 1

        return ans