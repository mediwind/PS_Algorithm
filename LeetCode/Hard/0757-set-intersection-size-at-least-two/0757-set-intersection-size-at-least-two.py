class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        INF_NEG = -10**18
        intervals.sort(key=lambda iv: (iv[1], -iv[0]))
        last1 = last2 = INF_NEG
        ans = 0
        for a, b in intervals:
            if last1 < a:
                ans += 2
                last2 = b - 1
                last1 = b
            elif last2 < a:
                ans += 1
                last2 = last1
                last1 = b
            
        return ans