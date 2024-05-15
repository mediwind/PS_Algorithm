class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = list()
        for p in path:
            if p == '':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.':
                continue
            elif p == '/':
                continue
            else:
                stack.append(p)
        
        while stack and stack[-1] == '/':
            stack.pop()
        while stack and stack[0] == '/':
            stack.pop(0)
        # print(stack)
        
        return '/' + '/'.join(stack)