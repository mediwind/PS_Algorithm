class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        
        def to_base(a, b):
            res = list()
            
            while a:
                tmp = a % b
                res.append(str(tmp))
                a //= b
            
            return ''.join(res)[::-1]
        

        def is_palindromic(word):
            return word == word[::-1]


        for i in range(2, n - 2 + 1):
            number = to_base(n, i)
            if not is_palindromic(number):
                return False
        
        return True