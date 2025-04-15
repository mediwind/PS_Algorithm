# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 트리가 비어있으면 깊이는 0

        # BFS를 사용하여 최소 깊이를 찾음
        deque = collections.deque
        Q = deque([(root, 1)])  # (노드, 깊이) 형태로 저장
        while Q:
            node, depth = Q.popleft()
            
            # 리프 노드에 도달하면 현재 깊이를 반환
            if not node.left and not node.right:
                return depth
            
            # 왼쪽 자식이 있으면 큐에 추가
            if node.left:
                Q.append((node.left, depth + 1))
            
            # 오른쪽 자식이 있으면 큐에 추가
            if node.right:
                Q.append((node.right, depth + 1))