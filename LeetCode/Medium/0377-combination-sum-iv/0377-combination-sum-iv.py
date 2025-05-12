class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dy = [0 for _ in range(target + 1)]
        dy[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dy[i] += dy[i - num]
        
        return dy[target]