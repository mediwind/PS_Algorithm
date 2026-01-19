class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row_count, col_count = len(mat), len(mat[0])

        prefix_sum = [[0] * (col_count + 1) for _ in range(row_count + 1)]

        for r in range(1, row_count + 1):
            for c in range(1, col_count + 1):
                prefix_sum[r][c] = (
                    mat[r - 1][c - 1]
                    + prefix_sum[r - 1][c]
                    + prefix_sum[r][c - 1]
                    - prefix_sum[r - 1][c - 1]
                )

        max_side_length = min(row_count, col_count)

        while max_side_length > 0:
            for r in range(row_count - max_side_length + 1):
                for c in range(col_count - max_side_length + 1):
                    square_sum = (
                        prefix_sum[r + max_side_length][c + max_side_length]
                        - prefix_sum[r][c + max_side_length]
                        - prefix_sum[r + max_side_length][c]
                        + prefix_sum[r][c]
                    )
                    if square_sum <= threshold:
                        return max_side_length
            max_side_length -= 1

        return 0