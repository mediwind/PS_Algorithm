class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        mal_key = set(brokenLetters)
        ans = 0
        for word in words:
            for ch in word:
                if ch in mal_key:
                    break
            else:
                ans += 1
        
        return ans