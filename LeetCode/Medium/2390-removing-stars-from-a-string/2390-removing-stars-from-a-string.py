class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
        
        return ''.join(stack)