# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Q = deque()
        Q.append(root)

        answer = list()
        while Q:
            res = 0
            Qleng = len(Q)
            for _ in range(Qleng):
                node = Q.popleft()
                res += node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            
            answer.append(res/Qleng)
        
        return answer