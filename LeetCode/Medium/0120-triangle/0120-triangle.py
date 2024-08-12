class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dy = [0 for _ in range(n + 1)]

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dy[i] = n + min(dy[i], dy[i + 1])
        
        return dy[0]