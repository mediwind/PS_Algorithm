class Solution:
    def kthCharacter(self, k: int) -> str:
        words = 'a'

        while len(words) < k:
            tmp = ''
            for word in words:
                tmp += chr((ord(word) + 1)) if ord(word) + 1 <= ord('z') else 'a'

            words += tmp
        
        return words[k - 1]