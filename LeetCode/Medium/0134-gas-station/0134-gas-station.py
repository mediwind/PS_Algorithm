class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        
        start, tank = 0, 0
        for i in range(n):
            if tank + gas[i] < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]
        
        return start