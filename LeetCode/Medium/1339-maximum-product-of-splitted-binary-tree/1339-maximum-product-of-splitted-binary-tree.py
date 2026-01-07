# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def DFS(node):
            if node is None:
                return 0
            
            subtree_sum = DFS(node.left) + DFS(node.right) + node.val
            sums.append(subtree_sum)

            return subtree_sum

        sums = list()
        
        m = float('-inf')
        total = DFS(root)
        for i in sums:
            prod = i * (total - i)
            if prod > m:
                m = prod
        
        return m % (10 ** 9 + 7)
