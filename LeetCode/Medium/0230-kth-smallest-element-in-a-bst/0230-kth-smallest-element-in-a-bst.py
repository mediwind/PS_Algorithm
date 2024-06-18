# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = set()

        Q = deque()
        Q.append(root)
        while Q:
            node = Q.popleft()
            answer.add(node.val)
            if node.left:
                answer.add(node.left.val)
                Q.append(node.left)
            if node.right:
                answer.add(node.right.val)
                Q.append(node.right)
        
        answer = sorted(list(answer))
        return answer[k - 1]