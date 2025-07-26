"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
            
        ans = list()

        Q = collections.deque()
        Q.append(root)
        while Q:
            level = list()
            for _ in range(len(Q)):
                node = Q.popleft()
                level.append(node.val)
                if node.children:
                    Q.extend(node.children)
            ans.append(level)
        
        return ans
