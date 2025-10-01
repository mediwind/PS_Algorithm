class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empties = numBottles
        
        while empties >= numExchange:
            new = empties // numExchange
            total += new
            empties = empties % numExchange + new

        return total