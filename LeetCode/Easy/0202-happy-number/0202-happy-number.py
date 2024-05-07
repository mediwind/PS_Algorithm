class Solution:
    def isHappy(self, n: int) -> bool:
        ch = set()
        while True:
            intToStr = str(n)
            res = 0
            for num in intToStr:
                res += int(num) ** 2
            
            if res == 1:
                return True
            
            if res not in ch:
                ch.add(res)
                n = res
            else:
                return False