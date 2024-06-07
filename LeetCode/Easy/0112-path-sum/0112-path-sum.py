# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        Q = [(root, targetSum - root.val)]
        while Q:
            node, curr_sum = Q.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                Q.append((node.right, curr_sum - node.right.val))
            if node.left:
                Q.append((node.left, curr_sum - node.left.val))
        
        return False