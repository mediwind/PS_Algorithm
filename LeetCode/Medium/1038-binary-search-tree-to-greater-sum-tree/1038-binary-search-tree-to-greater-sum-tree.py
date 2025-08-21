# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def rev_inorder(node):
            nonlocal total
            if not node:
                return
            rev_inorder(node.right)
            total += node.val
            node.val = total
            rev_inorder(node.left)
            
        rev_inorder(root)
        return root