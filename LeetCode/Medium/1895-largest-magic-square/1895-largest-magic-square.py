class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        row_count, col_count = len(grid), len(grid[0])
        max_size = 1

        def is_valid_square(start_row, start_col, size):
            target_sum = None

            for r in range(start_row, start_row + size):
                row_sum = sum(grid[r][start_col:start_col + size])
                if target_sum is None:
                    target_sum = row_sum
                elif row_sum != target_sum:
                    return False

            for c in range(start_col, start_col + size):
                col_sum = sum(grid[r][c] for r in range(start_row, start_row + size))
                if col_sum != target_sum:
                    return False

            diag_sum_1 = sum(
                grid[start_row + d][start_col + d] for d in range(size)
            )
            if diag_sum_1 != target_sum:
                return False

            diag_sum_2 = sum(
                grid[start_row + d][start_col + size - 1 - d]
                for d in range(size)
            )
            if diag_sum_2 != target_sum:
                return False

            return True

        for size in range(2, min(row_count, col_count) + 1):
            for r in range(row_count - size + 1):
                for c in range(col_count - size + 1):
                    if is_valid_square(r, c, size):
                        max_size = size

        return max_size