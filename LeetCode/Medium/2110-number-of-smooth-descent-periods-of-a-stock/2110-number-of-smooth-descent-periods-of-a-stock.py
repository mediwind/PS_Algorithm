class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total, target, prev = 0, 0, -1
        for price in prices:
            target = (-((price + 1) == prev) & target) + 1
            total += target
            prev = price
        
        return total