class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        a = sorted(happiness, reverse=True)
        total = 0
        for i in range(k):
            if i >= len(a):
                break
            val = a[i] - i
            if val > 0:
                total += val
                
        return total