class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row_count, col_count = len(matrix), len(matrix[0])

        for r in range(1, row_count):
            for c in range(col_count):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]

        max_area = 0

        for r in range(row_count):
            sorted_heights = sorted(matrix[r])

            for idx in range(col_count):
                height = sorted_heights[idx]
                width = col_count - idx
                max_area = max(max_area, height * width)

        return max_area