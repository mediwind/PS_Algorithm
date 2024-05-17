class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(t)
            else:
                b, a = stack.pop(), stack.pop()
                # The division between two integers always truncates toward zero.
                # 소수점이 0의 방향으로 수렴되게 하려면 floor()가 아닌 int()
                res = int(eval(''.join([a, t, b])))
                stack.append(str(res))
        
        return int(stack[0])