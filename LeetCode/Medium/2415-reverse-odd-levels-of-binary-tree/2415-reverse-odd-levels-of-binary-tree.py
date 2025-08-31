# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deque = collections.deque

        Q = deque()
        Q.append(root)
        floor = 0

        while Q:
            level_nodes = list()
            
            for _ in range(len(Q)):
                node = Q.popleft()
                level_nodes.append(node)

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                
            if floor % 2:
                arr = [level_node.val for level_node in level_nodes]
                arr.reverse()
                for idx, node in enumerate(level_nodes):
                    node.val = arr[idx]
            
            floor += 1

        return root