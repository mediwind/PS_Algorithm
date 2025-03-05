class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            tmp = abs(ord(s[i - 1]) - ord(s[i]))
            ans += tmp
        
        return ans