class Solution:

    def __init__(self, nums: List[int]):
        self.idx_map = {}
        for i, num in enumerate(nums):
            if num not in self.idx_map:
                self.idx_map[num] = []
            self.idx_map[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.idx_map[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)