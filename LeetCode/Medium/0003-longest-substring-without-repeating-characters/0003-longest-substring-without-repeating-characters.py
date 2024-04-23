class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        lt = 0
        res = 0

        for rt in range(len(s)):
            while s[rt] in charSet:
                charSet.remove(s[lt])
                lt += 1
            charSet.add(s[rt])
            res = max(res, rt - lt + 1)
        
        return res