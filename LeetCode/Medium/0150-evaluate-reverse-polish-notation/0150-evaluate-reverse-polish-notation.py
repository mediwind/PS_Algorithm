from math import ceil, floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(t)
            else:
                b, a = stack.pop(), stack.pop()
                res = int(eval(''.join([a, t, b])))
                stack.append(str(res))
        
        return int(stack[0])