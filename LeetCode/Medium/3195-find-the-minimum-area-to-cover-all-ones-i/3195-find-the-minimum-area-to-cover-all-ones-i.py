class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        min_r, max_r = rows, -1
        min_c, max_c = cols, -1

        for i in range(rows):
            row = grid[i]
            for j, val in enumerate(row):
                if val == 1:
                    if i < min_r: min_r = i
                    if i > max_r: max_r = i
                    if j < min_c: min_c = j
                    if j > max_c: max_c = j

        # 모든 1이 존재한다고 문제에서 보장하므로 별도 검사 생략 가능
        height = max_r - min_r + 1
        width  = max_c - min_c + 1
        return height * width