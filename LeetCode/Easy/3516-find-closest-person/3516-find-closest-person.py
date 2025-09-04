class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        res1 = abs(x - z)
        res2 = abs(y - z)

        if res1 < res2:
            return 1
        elif res1 > res2:
            return 2
        else:
            return 0