class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = list()

        for xj, yj, rj in queries:
            cnt = 0
            for xi, yi, in points:
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= rj ** 2:
                    cnt += 1
            res.append(cnt)
        
        return res