class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        to_skip = set()
        for i in range(n):
            if 1 <= i < n - 1:
                if s[i - 1] == s[i] == s[i + 1]:
                    to_skip.add(i)
        
        ans = ''
        for i in range(n):
            if i not in to_skip:
                ans += s[i]
        
        return ans
