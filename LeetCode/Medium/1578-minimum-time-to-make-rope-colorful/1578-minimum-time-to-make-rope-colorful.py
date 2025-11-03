class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        group_sum = 0
        group_max = 0
        prev = ''
        for c, t in zip(colors, neededTime):
            if c != prev:
                total += group_sum - group_max
                group_sum = t
                group_max = t
                prev = c
            else:
                group_sum += t
                if t > group_max:
                    group_max = t
                    
        total += group_sum - group_max
        return total