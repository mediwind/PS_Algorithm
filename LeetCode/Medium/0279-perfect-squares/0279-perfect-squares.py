class Solution:
    def numSquares(self, n: int) -> int:
        dy = [float("inf") for _ in range(n + 1)]
        dy[0] = 0

        squares = list()
        for i in range(1, int(n ** 0.5) + 1):
            squares.append(i ** 2)
        
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dy[i] = min(dy[i], dy[i - square] + 1)
        
        return dy[n]