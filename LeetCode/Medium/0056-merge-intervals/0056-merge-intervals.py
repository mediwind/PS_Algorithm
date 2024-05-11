class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:(x[0], x[1]))
        n = len(intervals)
        ans = list()
        start, end = intervals[0]
        for i in range(1, n):
            if intervals[i][0] <= end:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start, end = intervals[i]
        
        ans.append([start, end])
        return ans