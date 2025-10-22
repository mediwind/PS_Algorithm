class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        from collections import Counter

        n = len(nums)
        events = []
        for v in nums:
            L = v - k
            R = v + k
            events.append((L, 1))
            events.append((R + 1, -1))
        events.sort()
        
        max_seg = 0
        cov = 0
        i = 0
        prev = None
        m = len(events)
        while i < m:
            pos = events[i][0]
            if prev is not None and pos > prev:
                if cov > max_seg:
                    max_seg = cov

            while i < m and events[i][0] == pos:
                cov += events[i][1]
                i += 1

            prev = pos

        if cov > max_seg:
            max_seg = cov

        freq = Counter(nums)
        uniq = sorted(freq)
        cov = 0
        i = 0
        best = 0
        for x in uniq:

            while i < m and events[i][0] <= x:
                cov += events[i][1]
                i += 1
            base = freq[x]
            val = cov
            cand = min(val, base + numOperations)

            if cand > best:
                best = cand

        seg_cand = min(max_seg, numOperations)
        
        return max(best, seg_cand)