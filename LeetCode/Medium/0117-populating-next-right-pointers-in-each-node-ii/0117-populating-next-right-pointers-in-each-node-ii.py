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
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return

        Q = deque([root])
        while Q:
            len_queue = len(Q)
            pre = None
            for _ in range(len_queue):
                temp = Q.popleft()
                if temp.left:
                    Q.append(temp.left)
                if temp.right:
                    Q.append(temp.right)
                if pre:
                    pre.next = temp
                pre = temp
            pre.next = None
        
        return root