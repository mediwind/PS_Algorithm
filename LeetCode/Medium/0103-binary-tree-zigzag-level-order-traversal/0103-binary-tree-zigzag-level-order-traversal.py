# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        answer = list()
        Q = deque()
        Q.append(root)
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
        
        for i in range(len(answer)):
            if i % 2:
                answer[i] = answer[i][::-1]

        return answer