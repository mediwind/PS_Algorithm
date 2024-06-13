# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = list()
        Q = deque()
        Q.append(root)

        while Q:
            rightSide = None
            Qleng = len(Q)

            for _ in range(Qleng):
                node = Q.popleft()
                if node:
                    rightSide = node
                    Q.append(node.left)
                    Q.append(node.right)
                
            if rightSide:
                answer.append(rightSide.val)
        
        return answer