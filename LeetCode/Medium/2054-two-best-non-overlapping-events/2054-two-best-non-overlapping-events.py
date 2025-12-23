class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        import bisect

        events.sort(key=lambda x: x[0])
        starts = [e[0] for e in events]
        n = len(events)
        vals = [e[2] for e in events]

        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], vals[i])

        ans = 0
        for i, (s, e, v) in enumerate(events):
            ans = max(ans, v)
            j = bisect.bisect_right(starts, e)  # first event with start > e
            if j < n:
                ans = max(ans, v + suffix_max[j])

        return ans