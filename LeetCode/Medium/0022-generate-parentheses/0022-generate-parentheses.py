class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def DFS(openN, closedN):
            if openN == closedN == n:
                ans.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                DFS(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                DFS(openN, closedN + 1)
                stack.pop()
        
        stack = list()
        ans = list()
        DFS(0, 0)
        return ans