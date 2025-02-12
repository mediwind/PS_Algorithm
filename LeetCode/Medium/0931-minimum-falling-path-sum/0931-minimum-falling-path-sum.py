class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dy = [[0 for _ in range(n)] for _ in range(n)]
        dy[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                mini = float("inf")
                for k in [-1, 0, 1]:
                    if j + k < 0 or j + k >= n:
                        continue
                    mini = min(mini, matrix[i][j] + dy[i - 1][j + k])
                    dy[i][j] = mini

        return min(dy[-1])