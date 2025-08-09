class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n # dp[i]: nums[i]를 끝으로 하는 최대 부분집합 크기
        prev = [-1] * n # prev[i]: nums[i] 앞에 붙일 인덱스

        max_len = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # 부분집합 역추적
        res = []
        idx = max_idx
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]
            
        return res[::-1]