class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        ans = s.count('0')

        ones = list()
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                ones.append(i)
        
        res = 0
        for idx in ones:
            res += 2 ** (n - 1 - idx)
            if res > k:
                break
            ans += 1
        
        return ans