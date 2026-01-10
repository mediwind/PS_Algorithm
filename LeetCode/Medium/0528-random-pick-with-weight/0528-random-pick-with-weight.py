class Solution:
    import random
    
    def __init__(self, w: List[int]):
        self.weights = w

        total_weight = sum(self.weights)
        for i in range(len(self.weights)):
            self.weights[i] /= total_weight

        for i in range(1, len(self.weights)):
            self.weights[i] += self.weights[i - 1]

    def pickIndex(self) -> int:
        random_value = random.uniform(0, 1)

        current_index = 0
        while random_value > self.weights[current_index]:
            current_index += 1

        return current_index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()