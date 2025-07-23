class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_pair(s, first, second, score):
            stack = list()
            total = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(c)

            return total, ''.join(stack)
        
        ans = 0
        if x > y:
            ans, s = remove_pair(s, 'a', 'b', x)
            res, s = remove_pair(s, 'b', 'a', y)
        else:
            ans, s = remove_pair(s, 'b', 'a', y)
            res, s = remove_pair(s, 'a', 'b', x)
        
        return ans + res