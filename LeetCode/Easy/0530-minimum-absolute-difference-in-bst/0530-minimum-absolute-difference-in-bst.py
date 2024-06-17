# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = set()
        nodes.add(root.val)
        Q = deque()
        Q.append(root)
        while Q:
            node = Q.popleft()
            if node.left:
                nodes.add(node.left.val)
                Q.append(node.left)
            if node.right:
                nodes.add(node.right.val)
                Q.append(node.right)
        
        nodes = sorted(list(set(nodes)))
        print(nodes)
        answer = float('inf')
        for i in range(len(nodes) - 1):
            answer = min(answer, nodes[i + 1] - nodes[i])
        return answer