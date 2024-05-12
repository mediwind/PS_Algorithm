class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        
        ans = list()
        n = len(intervals)
        start, end = intervals[0]
        for i in range(1, n):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start, end = intervals[i]
        
        ans.append([start, end])
        return ans