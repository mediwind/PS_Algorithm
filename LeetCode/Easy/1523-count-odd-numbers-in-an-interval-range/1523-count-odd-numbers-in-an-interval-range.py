class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        # counting even numbers between low and high
        ans = (high - low) // 2
        # plus 1 if low or high is odd number
        if low % 2 or high % 2:
            ans += 1
        
        return ans