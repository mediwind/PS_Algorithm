# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def DFS(lt, rt):
            if lt > rt:
                return None
            
            mid = (lt + rt) // 2
            root = TreeNode(nums[mid])
            root.left = DFS(lt, mid - 1)
            root.right = DFS(mid + 1, rt)
            return root
        
        return DFS(0, len(nums) - 1)