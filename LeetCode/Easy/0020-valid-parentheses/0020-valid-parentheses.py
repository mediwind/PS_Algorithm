class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = list()
        for i in range(n):
            if s[i] in ("(", "{", "["):
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif s[i] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif s[i] == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                elif s[i] == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        
        if stack:
            return False
        else:
            return True