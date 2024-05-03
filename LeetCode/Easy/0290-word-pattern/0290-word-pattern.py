class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        words = s.split()

        if n != len(words):
            return False

        charToWord = dict()
        wordToChar = dict()
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
    
        return True