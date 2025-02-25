# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return list()
        
        def generateTrees(start, end):
            if start > end:
                return [None]
            
            all_trees = list()
            for i in range(start, end + 1):
                # 모든 가능한 왼쪽 서브트리 생성
                left_trees = generateTrees(start, i - 1)
                # 모든 가능한 오른쪽 서브트리 생성
                right_trees = generateTrees(i + 1, end)
                
                # 모든 왼쪽 서브트리와 오른쪽 서브트리 조합
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generateTrees(1, n)