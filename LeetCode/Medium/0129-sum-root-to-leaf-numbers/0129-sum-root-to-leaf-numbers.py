# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def DFS(root, curr_sum):
            nonlocal answer

            if not root:
                return ""
            
            curr_sum += str(root.val)
            if not root.left and not root.right:
                answer += int(curr_sum)
            DFS(root.left, curr_sum)
            DFS(root.right, curr_sum)
        
        DFS(root, "")
        return answer