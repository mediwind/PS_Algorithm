class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')

        vowel_chars = [c for c in s if c in vowels]
        vowel_chars.sort()

        res = list()
        idx = 0
        for c in s:
            if c in vowels:
                res.append(vowel_chars[idx])
                idx += 1
            else:
                res.append(c)
                
        return ''.join(res)