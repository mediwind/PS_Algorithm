class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If a character is present in one word and not in the other (or vice versa), return false.
        if set(word1) != set(word2):
            return False

        # the order of frequencies doesn't matter, only their values.
        if sorted(list(Counter(word1).values())) != sorted(list(Counter(word2).values())):
            return False
        
        return True