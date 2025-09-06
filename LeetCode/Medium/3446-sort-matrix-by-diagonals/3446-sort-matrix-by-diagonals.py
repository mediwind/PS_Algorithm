class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for d in range(n):
            diag = []
            for i in range(d, n):
                j = i - d
                diag.append(grid[i][j])
            diag.sort(reverse=True)
            for idx, i in enumerate(range(d, n)):
                j = i - d
                grid[i][j] = diag[idx]
        
        for d in range(1, n):
            diag = []
            for i in range(n - d):
                j = i + d
                diag.append(grid[i][j])
            diag.sort()
            for idx, i in enumerate(range(n - d)):
                j = i + d
                grid[i][j] = diag[idx]
                
        return grid