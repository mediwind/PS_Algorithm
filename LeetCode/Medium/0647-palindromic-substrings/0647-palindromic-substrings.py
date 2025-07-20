class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def expand(lt, rt):
            nonlocal ans
            while lt >= 0 and rt < n and s[lt] == s[rt]:
                lt -= 1
                rt += 1
                ans += 1
            return
        
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        
        return ans