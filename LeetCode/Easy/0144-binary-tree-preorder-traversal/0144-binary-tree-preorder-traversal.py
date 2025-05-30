# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()
        

        def DFS(node):
            ans.append(node.val)

            if node.left:
                DFS(node.left)
            if node.right:
                DFS(node.right)
        

        ans = list()
        DFS(root)
        return ans