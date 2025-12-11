class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_max = [0] * (n + 1)
        row_min = [n + 1] * (n + 1)
        col_max = [0] * (n + 1)
        col_min = [n + 1] * (n + 1)

        for x, y in buildings:
            row_max[x] = max(row_max[x], y)
            row_min[x] = min(row_min[x], y)
            col_max[y] = max(col_max[y], x)
            col_min[y] = min(col_min[y], x)
        
        ans = 0
        for x, y in buildings:
            if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
                ans += 1
        
        return ans