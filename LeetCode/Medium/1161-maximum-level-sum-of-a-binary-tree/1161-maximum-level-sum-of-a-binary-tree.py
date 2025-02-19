# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        Q = deque()
        Q.append(root)

        maxi = root.val
        ans_floor = 1
        now_floor = 1
        while Q:
            lenQ = len(Q)
            floor_sum = 0
            for _ in range(lenQ):
                node = Q.popleft()
                floor_sum += node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            
            if maxi < floor_sum:
                maxi = floor_sum
                ans_floor = now_floor
            
            now_floor += 1
        
        return ans_floor