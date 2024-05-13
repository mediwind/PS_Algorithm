class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], x[1]))
        n = len(points)
        
        ans = 1
        start, end = points[0]
        for i in range(1, n):
            if points[i][0] <= end:
                start = max(start, points[i][0])
                end = min(end, points[i][1])
            if points[i][0] > end:
                ans += 1
                start, end = points[i]
        
        return ans