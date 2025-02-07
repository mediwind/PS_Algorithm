# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return list()


        def InOrder(x):
            if x == None:
                return
            
            InOrder(x.left)
            ans.append(x.val)
            InOrder(x.right)
        
        ans = list()
        InOrder(root)
        return ans
