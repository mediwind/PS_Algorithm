# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def DFS(num):
            if num % 2 == 0:
                return []
            if num == 1:
                return [TreeNode(0)]
            if num in memo:
                return memo[num]
            
            res = list()
            for left in range(1, num, 2):
                right = num - 1 - left
                for l in DFS(left):
                    for r in DFS(right):
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            memo[num] = res
            return res

        memo = dict()
        return DFS(n)