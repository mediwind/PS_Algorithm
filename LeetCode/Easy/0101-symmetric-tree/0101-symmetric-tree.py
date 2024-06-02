# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        LQ = deque()
        RQ = deque()

        LQ.append(root.left)
        RQ.append(root.right)

        while LQ and RQ:
            nodeLeft, nodeRight = LQ.popleft(), RQ.popleft()
            if not nodeLeft and not nodeRight:
                continue
            if not nodeLeft or not nodeRight or nodeLeft.val != nodeRight.val:
                return False
            
            LQ.append(nodeLeft.left)
            LQ.append(nodeLeft.right)

            RQ.append(nodeRight.right)
            RQ.append(nodeRight.left)
        
        if LQ or RQ:
            return False
        else:
            return True