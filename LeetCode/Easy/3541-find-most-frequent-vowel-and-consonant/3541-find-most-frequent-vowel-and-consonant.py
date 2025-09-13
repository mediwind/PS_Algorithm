class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_maxi = consonant_maxi = 0
        
        counter = collections.Counter(s)

        for key, val in counter.items():
            if key in {'a', 'e', 'i', 'o', 'u'}:
                if val > vowel_maxi:
                    vowel_maxi = val
            else:
                if val > consonant_maxi:
                    consonant_maxi = val
        
        return vowel_maxi + consonant_maxi