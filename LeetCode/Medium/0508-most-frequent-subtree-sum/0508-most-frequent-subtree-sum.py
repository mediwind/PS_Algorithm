# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()

        # 서브트리 합계의 빈도를 저장할 Counter
        subtree_sum_count = Counter()

        def calculate_subtree_sum(node):
            """현재 노드의 서브트리 합계를 계산하는 함수"""
            if not node:
                return 0  # 노드가 없으면 합계는 0
            # 왼쪽과 오른쪽 서브트리의 합계를 재귀적으로 계산
            left_sum = calculate_subtree_sum(node.left)
            right_sum = calculate_subtree_sum(node.right)
            # 현재 노드의 서브트리 합계 계산
            total_sum = node.val + left_sum + right_sum
            # 서브트리 합계의 빈도를 증가
            subtree_sum_count[total_sum] += 1
            return total_sum

        # 루트 노드부터 서브트리 합계 계산 시작
        calculate_subtree_sum(root)

        # 가장 높은 빈도를 찾음
        max_frequency = max(subtree_sum_count.values())

        # 최대 빈도를 가진 서브트리 합계를 결과 리스트에 추가
        result = [s for s, freq in subtree_sum_count.items() if freq == max_frequency]

        return result