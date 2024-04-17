class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for x in s:
            if x.isalnum():
                string += x
        
        string = string.lower()
        return string == string[::-1]