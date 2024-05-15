class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for p in path:
            if stack and p == "..":
                stack.pop()
            elif p not in [".", "", ".."]:
                stack.append(p)
                
        return "/" + "/".join(stack)