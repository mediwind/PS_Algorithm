# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right    # We go to left Subtree's rightMost Node
                
                prev.right = cur.right   #We make current Node's right Subtree prev's right Subtree
                cur.right = cur.left    # We make it right Subtree
                cur.left = None   # Removing left 
            
            cur = cur.right