class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        from collections import defaultdict
        
        row_count, col_count = len(grid), len(grid[0])

        value_positions = defaultdict(list)
        for row in range(row_count):
            for col in range(col_count):
                value_positions[grid[row][col]].append((row, col))

        infinity = float("inf")
        cost_dp = [[infinity] * col_count for _ in range(row_count)]
        cost_dp[0][0] = 0

        def relax_dp():
            for row in range(row_count):
                for col in range(col_count):
                    min_prev = min(
                        cost_dp[row - 1][col] if row > 0 else infinity,
                        cost_dp[row][col - 1] if col > 0 else infinity,
                    )
                    new_cost = grid[row][col] + min_prev
                    if new_cost < cost_dp[row][col]:
                        cost_dp[row][col] = new_cost

        relax_dp()

        sorted_values = sorted(value_positions.keys(), reverse=True)

        for _ in range(k):
            best_so_far = infinity
            for value in sorted_values:
                for row, col in value_positions[value]:
                    if cost_dp[row][col] < best_so_far:
                        best_so_far = cost_dp[row][col]
                for row, col in value_positions[value]:
                    cost_dp[row][col] = best_so_far
            relax_dp()

        return cost_dp[-1][-1]