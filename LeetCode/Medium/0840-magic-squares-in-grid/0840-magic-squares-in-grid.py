class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0]) if R else 0

        if R < 3 or C < 3:
            return 0

        target_set = set(range(1,10))
        cnt = 0
        for r in range(R-2):
            for c in range(C-2):
                vals = [grid[r+i][c+j] for i in range(3) for j in range(3)]
                if set(vals) != target_set:
                    continue
                ok = True
                for i in range(3):
                    if sum(grid[r+i][c+cj] for cj in range(3)) != 15:
                        ok = False; break
                if not ok:
                    continue
                for j in range(3):
                    if sum(grid[r+ri][c+j] for ri in range(3)) != 15:
                        ok = False; break
                if not ok:
                    continue
                if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                    continue
                if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                    continue
                cnt += 1

        return cnt