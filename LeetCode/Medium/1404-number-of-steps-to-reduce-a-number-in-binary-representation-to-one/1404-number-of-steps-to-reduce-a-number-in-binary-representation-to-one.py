class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        tmp = 0
        n = len(s)
        for i in range(n - 1, 0, -1):
            if int(s[i]) + tmp == 1:
                tmp = 1
                ans += 2
            else:
                ans += 1

        return ans + tmp