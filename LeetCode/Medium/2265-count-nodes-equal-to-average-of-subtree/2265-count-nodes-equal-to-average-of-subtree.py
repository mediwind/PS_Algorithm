# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def DFS(node):
            nonlocal ans

            if not node:
                return (0, 0) # sum, count

            ls, lc = DFS(node.left)
            rs, rc = DFS(node.right)
            s = ls + rs + node.val
            c = lc + rc + 1

            if s // c == node.val:
                ans += 1

            return (s, c)

        DFS(root)
        return ans