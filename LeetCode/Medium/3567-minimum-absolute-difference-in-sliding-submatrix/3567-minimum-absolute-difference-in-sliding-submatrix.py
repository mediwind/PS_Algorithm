class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        result = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

        for top in range(rows - k + 1):
            for left in range(cols - k + 1):

                values = set()

                # k x k 영역 수집
                for i in range(top, top + k):
                    for j in range(left, left + k):
                        values.add(grid[i][j])

                # 원소가 1개면 차이 0
                if len(values) <= 1:
                    result[top][left] = 0
                    continue

                sorted_values = sorted(values)

                min_diff = float('inf')

                for i in range(len(sorted_values) - 1):
                    diff = sorted_values[i + 1] - sorted_values[i]
                    min_diff = min(min_diff, diff)

                result[top][left] = min_diff

        return result