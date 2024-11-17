# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        def DFS(node, deep, dir):
            self.maxLength = max(self.maxLength, deep)

            if node.left is not None:
                if dir != 'left':
                    DFS(node.left, deep+1,'left')
                else:
                    DFS(node.left, 1, 'left')
            if node.right is not None:
                if dir != 'right':
                    DFS(node.right, deep+1, 'right')
                else:
                    DFS(node.right, 1, 'right')

        DFS(root, 0, '')
        
        return self.maxLength