class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(y, y + k - 1 + 1):
            for j in range(k // 2):
                grid[x + j][i], grid[x + k - j - 1][i] = grid[x + k - j - 1][i], grid[x + j][i]
        
        return grid