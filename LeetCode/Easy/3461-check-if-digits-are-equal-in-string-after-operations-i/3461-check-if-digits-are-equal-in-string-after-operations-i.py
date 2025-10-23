class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(c) for c in s]
        while len(digits) > 2:
            digits = [(digits[i] + digits[i+1]) % 10 for i in range(len(digits)-1)]
            
        return digits[0] == digits[1]