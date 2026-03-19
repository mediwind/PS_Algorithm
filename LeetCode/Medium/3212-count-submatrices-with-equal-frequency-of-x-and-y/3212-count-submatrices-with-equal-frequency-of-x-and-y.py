class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        col_prefix_x = [0] * cols
        col_prefix_y = [0] * cols

        valid_submatrix_count = 0

        for row in range(rows):
            row_running_x = 0
            row_running_y = 0

            for col in range(cols):
                if grid[row][col] == 'X':
                    row_running_x += 1
                elif grid[row][col] == 'Y':
                    row_running_y += 1

                col_prefix_x[col] += row_running_x
                col_prefix_y[col] += row_running_y

                if col_prefix_x[col] > 0 and col_prefix_x[col] == col_prefix_y[col]:
                    valid_submatrix_count += 1

        return valid_submatrix_count