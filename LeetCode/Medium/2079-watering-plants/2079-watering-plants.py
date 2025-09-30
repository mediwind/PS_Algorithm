class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        cur = capacity
        for i, p in enumerate(plants):
            if cur < p:
                steps += 2 * i
                cur = capacity
            steps += 1
            cur -= p
            
        return steps