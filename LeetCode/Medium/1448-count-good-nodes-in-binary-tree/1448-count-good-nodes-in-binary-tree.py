# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def DFS(self, node, maxi):
        if not node:
            return
        
        if node.val >= maxi:
            self.ans += 1
        
        maxi = max(maxi, node.val)

        self.DFS(node.left, maxi)
        self.DFS(node.right, maxi)

    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.DFS(root, root.val)
        return self.ans