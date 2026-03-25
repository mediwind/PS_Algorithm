class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        total_sum = sum(sum(row) for row in grid)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        running = 0
        for i in range(m - 1):
            running += sum(grid[i])
            if running == target:
                return True

        col_sum = [0] * n
        for r in range(m):
            for c in range(n):
                col_sum[c] += grid[r][c]

        running = 0
        for j in range(n - 1):
            running += col_sum[j]
            if running == target:
                return True

        return False