# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            # 노드가 없으면 높이는 0, 균형 잡힘
            if not node:
                return 0, True
            
            # 왼쪽 서브트리 높이와 균형 여부 확인
            left_height, left_balanced = check_balance(node.left)
            # 오른쪽 서브트리 높이와 균형 여부 확인
            right_height, right_balanced = check_balance(node.right)
            
            # 현재 노드의 균형 여부 확인
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            
            # 현재 노드의 높이 계산
            height = max(left_height, right_height) + 1
            
            return height, balanced
        
        # 루트 노드에서 균형 여부 확인
        _, is_balanced = check_balance(root)
        return is_balanced