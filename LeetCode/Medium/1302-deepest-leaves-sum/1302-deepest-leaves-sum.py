# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        Q = deque([root])
        while Q:
            level_sum = 0
            for _ in range(len(Q)):
                node = Q.popleft()
                level_sum += node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                    
        return level_sum