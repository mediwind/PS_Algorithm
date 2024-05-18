class Solution:
    def calculate(self, s: str) -> int:
        now, res = 0, 0
        sign = 1
        
        stack = list()
        for c in s:
            if c.isdigit():
                now = now * 10 + int(c)
            elif c in "+-":
                res += sign * now
                
                if c == "+":
                    sign = 1
                else:
                    sign = -1
                
                now = 0
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                
                sign = 1
                
                res = 0
            elif c == ")":
                res += sign * now
                res *= stack.pop()
                res += stack.pop()
                now = 0
        
        return res + (sign * now)