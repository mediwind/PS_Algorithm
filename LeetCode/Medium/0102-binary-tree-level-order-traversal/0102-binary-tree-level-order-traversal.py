# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        Q = deque()
        Q.append(root)

        answer = list()
        while Q:
            Qleng = len(Q)
            tmp = list()
            for _ in range(Qleng):
                node = Q.popleft()
                tmp.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            answer.append(tmp)
        
        return answer