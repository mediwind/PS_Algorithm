class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0
        for char in columnTitle:
            num = ord(char) - 64
            ans = ans * 26 + num
        
        return ans