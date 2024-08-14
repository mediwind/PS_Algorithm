class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dy = [0 for _ in range(N)]
        dy[N - 1] = 1

        # Time: O(N * M), Space O(N)
        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]:
                    dy[c] = 0
                elif c + 1 < N:
                    dy[c] = dy[c] + dy[c + 1]
        
        return dy[0]