# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        
        if not root:
            return None

        parent_map = {root: None}
        queue = deque([root])
        deepest_nodes = []

        while queue:
            level_size = len(queue)
            deepest_nodes = []
            for _ in range(level_size):
                current_node = queue.popleft()
                deepest_nodes.append(current_node)

                if current_node.left:
                    parent_map[current_node.left] = current_node
                    queue.append(current_node.left)
                if current_node.right:
                    parent_map[current_node.right] = current_node
                    queue.append(current_node.right)

        candidates = set(deepest_nodes)

        while len(candidates) > 1:
            candidates = {parent_map[node] for node in candidates}

        return candidates.pop()
