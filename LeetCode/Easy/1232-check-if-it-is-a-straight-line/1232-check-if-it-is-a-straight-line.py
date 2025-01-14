class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        res = set()
        
        for i in range(n - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]
            if x2 == x1:
                res.add(float("inf"))
                continue
            tmp = (y2 - y1) / (x2 - x1)
            res.add(tmp)
        
        if len(res) >= 2:
            return False
        return True