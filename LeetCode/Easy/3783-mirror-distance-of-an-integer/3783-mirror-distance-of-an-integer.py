class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse, x = 0, n
        while x > 0:
            x, r = divmod(x, 10)
            reverse = 10 * reverse + r
        
        return abs(reverse - n)