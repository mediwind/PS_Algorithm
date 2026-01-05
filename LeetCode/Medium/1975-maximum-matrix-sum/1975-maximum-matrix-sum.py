class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        minus = 0
        min_abs = float('inf')

        for row in matrix:
            for col in row:
                if col < 0:
                    minus += 1
                num = abs(col)
                total += num
                min_abs = min(min_abs, num)
        
        if not minus % 2:
            return total
        
        return total - 2 * min_abs