class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))

        intervals = [(x - k, x + k) for x in nums]
        intervals.sort(key=lambda t: (t[1], t[0]))
        last = -10**30
        cnt = 0
        for l, r in intervals:
            x = max(l, last + 1)
            if x <= r:
                cnt += 1
                last = x
                
        return cnt