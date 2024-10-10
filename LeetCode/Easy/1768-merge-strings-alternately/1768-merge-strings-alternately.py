class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = ""
        for i in range(n):
            res += word1[i]
            res += word2[i]
        
        if i < len(word1) - 1:
            res += word1[i + 1:]
        if i < len(word2) - 1:
            res += word2[i + 1:]
        
        return res