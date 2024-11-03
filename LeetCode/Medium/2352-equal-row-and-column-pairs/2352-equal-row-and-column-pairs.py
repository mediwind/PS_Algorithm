class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        compared = list(map(list, zip(*grid)))
        grid = sorted(grid)
        compared = sorted(compared)
        
        cnt = 0
        for g in grid:
            for c in compared:
                if g == c:
                    cnt += 1
        
        return cnt