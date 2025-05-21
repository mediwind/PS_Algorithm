# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        

        def DFS(node, path, now_sum):
            if not node:
                return
            
            path.append(node.val)
            now_sum += node.val

            if not node.left and not node.right and now_sum == targetSum:
                ans.append(path[:])
            else:
                DFS(node.left, path, now_sum)
                DFS(node.right, path, now_sum)
            
            path.pop()
        
        ans = list()

        DFS(root, list(), 0)

        return ans