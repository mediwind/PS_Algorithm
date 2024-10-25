class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        n = len(s)
        lt, rt = 0, k - 1

        ans = 0
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        ans = cnt

        while rt < n:
            if s[lt] in vowels:
                cnt -= 1
            lt += 1
            rt += 1
            if rt == n:
                break
            if s[rt] in vowels:
                cnt += 1
            ans = max(ans, cnt)
        
        return ans
                