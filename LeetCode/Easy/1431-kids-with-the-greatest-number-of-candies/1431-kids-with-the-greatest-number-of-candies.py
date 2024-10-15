class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= maximum:
                res += [True]
            else:
                res += [False]
        
        return res