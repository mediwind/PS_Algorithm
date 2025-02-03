class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = list()
        for i in range(n - 2):
            res = list()
            for j in range(n - 2):
                tmp = float("-inf")
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        tmp = max(tmp, grid[k][l])
                res.append(tmp)
            ans.append(res)
        
        return ans