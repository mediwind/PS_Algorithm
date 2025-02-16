"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return

        def BFS(root):
            Q = collections.deque()
            Q.append((root, 0))

            res = list()
            while Q:
                node, level = Q.popleft()

                if not node:
                    continue

                res.append((node, level))

                if node.left:
                    Q.append((node.left, level + 1))
                if node.right:
                    Q.append((node.right, level + 1))

            return res

        res = BFS(root)

        n = len(res)
        for i in range(n - 1):
            node, level = res[i]
            if res[i + 1][1] == level:
                node.next = res[i + 1][0]
            else:
                node.next = None
        
        res[-1][0].next = None

        return root