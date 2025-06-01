# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        

        def DFS(node):
            if node.left:
                DFS(node.left)
            if node.right:
                DFS(node.right)
            if node:
                ans.append(node.val)
        
        ans = list()
        DFS(root)
        return ans