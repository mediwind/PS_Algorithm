class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        l = sorted((e[0], i) for i, e in enumerate(intervals))
        res = [-1 for _ in range(n)]

        for i, e in enumerate(intervals):
            r = bisect.bisect_left(l, (e[1],))
            if r < len(l):
                res[i] = l[r][1]

        return res