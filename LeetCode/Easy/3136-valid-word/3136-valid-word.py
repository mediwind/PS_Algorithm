class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
            
        vowels = {'a', 'e', 'i', 'o', 'u'}
        char = vowel = consonant = 0
        for w in word:
            w = w.lower()
            if w.isalpha():
                char += 1
                if w in vowels:
                    vowel += 1
                else:
                    consonant += 1
            elif w.isdigit():
                pass
            else:
                return False
        
        if vowel and consonant:
            return True
        
        return False