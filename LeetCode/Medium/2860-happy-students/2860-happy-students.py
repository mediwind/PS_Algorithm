class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        res = 0
        # 누구도 뽑지 않는 경우가 유효
        if nums[0] > 0:
            res += 1
        # 모두를 뽑는 경우가 유효
        if nums[-1] < n:
            res += 1
        
        for i in range(n - 1):
            if nums[i] < i + 1 < nums[i + 1]:
                res += 1
        
        return res