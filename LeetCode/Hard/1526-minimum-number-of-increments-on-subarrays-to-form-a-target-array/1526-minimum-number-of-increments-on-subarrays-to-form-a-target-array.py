class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0

        ans = target[0]
        for i in range(1, len(target)):
            d = target[i] - target[i-1]
            if d > 0:
                ans += d
                
        return ans