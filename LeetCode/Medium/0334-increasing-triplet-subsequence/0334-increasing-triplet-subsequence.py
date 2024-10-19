class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        maxRight = [0 for _ in range(n)]
        maxRight[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(nums[i + 1], maxRight[i + 1])
        
        minLeft = nums[0]
        for i in range(1, n):
            if minLeft < nums[i] < maxRight[i]:
                return True
            minLeft = min(minLeft, nums[i])

        return False