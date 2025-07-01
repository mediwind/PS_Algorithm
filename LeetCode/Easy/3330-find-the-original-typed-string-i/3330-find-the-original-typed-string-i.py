class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        
        return ans + 1