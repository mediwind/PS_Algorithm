# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def DFS(node):
            if not node:
                return (0, 0)
            
            rob_left, skip_left = DFS(node.left)
            rob_right, skip_right = DFS(node.right)

            rob_current_node = node.val + skip_left + skip_right
            skip_current_node = max(rob_left, skip_left) + max(rob_right, skip_right)

            return (rob_current_node, skip_current_node)

        rob_root, skip_root = DFS(root)

        return max(rob_root, skip_root)