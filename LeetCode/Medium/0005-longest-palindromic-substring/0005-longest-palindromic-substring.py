class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            lt, rt = i, i
            while lt >= 0 and rt < len(s) and s[lt] == s[rt]:
                if (rt - lt + 1) > resLen:
                    res = s[lt:rt + 1]
                    resLen = rt - lt + 1
                lt -= 1
                rt += 1
            
            # even length
            lt, rt = i, i + 1
            while lt >= 0 and rt < len(s) and s[lt] == s[rt]:
                if (rt - lt + 1) > resLen:
                    res = s[lt:rt + 1]
                    resLen = rt - lt + 1
                lt -= 1
                rt += 1
        
        return res