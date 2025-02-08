# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []


        def BFS(node, depth):
            Q = collections.deque()
            Q.append((node, depth))

            while Q:
                x, depth = Q.popleft()

                if len(res) == depth:
                    res.append(list())

                res[depth].append(x.val)
                
                if x.left:
                    Q.append((x.left, depth + 1))
                if x.right:
                    Q.append((x.right, depth + 1))


        res = []
        BFS(root, 0)

        return res[::-1]