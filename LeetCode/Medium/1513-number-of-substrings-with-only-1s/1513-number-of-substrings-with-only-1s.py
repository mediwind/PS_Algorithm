class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        cur = 0
        ans = 0
        for ch in s:
            if ch == '1':
                cur += 1
                ans = (ans + cur) % MOD
            else:
                cur = 0
                
        return ans