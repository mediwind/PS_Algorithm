# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            
            return self.DFS(node.left) + self.DFS(node.right)
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.DFS(root1) == self.DFS(root2)