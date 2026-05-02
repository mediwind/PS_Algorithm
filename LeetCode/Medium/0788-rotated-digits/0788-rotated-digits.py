class Solution:
    def rotatedDigits(self, n: int) -> int:
        bad = {'3', '4', '7'}
        good = {'2', '5', '6', '9'}
        ans = 0

        for x in range(1, n + 1):
            s = str(x)
            if any(c in bad for c in s):
                continue
            if any(c in good for c in s):
                ans += 1

        return ans