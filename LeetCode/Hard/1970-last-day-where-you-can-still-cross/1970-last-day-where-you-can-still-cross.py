class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        from collections import deque

        n = row * col
        cells0 = [(r-1, c-1) for r, c in cells]

        def can_cross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells0[i]
                grid[r][c] = 1

            q = deque()
            seen = [[False]*col for _ in range(row)]
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    seen[0][j] = True

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < row and 0 <= nc < col and not seen[nr][nc] and grid[nr][nc] == 0:
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return False

        lo, hi = 1, n
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_cross(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans