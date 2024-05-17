from math import ceil, floor


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for t in tokens:
            if is_number(t):
                stack.append(t)
            else:
                b, a = stack.pop(), stack.pop()
                res = eval(''.join([a, t, b]))
                if res >= 0:
                    res = floor(res)
                else:
                    res = ceil(res)
                stack.append(str(res))
        
        return int(stack[0])