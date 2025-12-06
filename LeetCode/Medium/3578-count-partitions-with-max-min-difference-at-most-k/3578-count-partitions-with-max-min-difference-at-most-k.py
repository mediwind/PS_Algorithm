class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        from collections import deque

        MOD = 10**9 + 7

        n = len(nums)
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = 1
        pref[0] = 1
        left = 0
        maxdq = deque()
        mindq = deque()
        for i in range(1, n + 1):
            x = nums[i - 1]
            while maxdq and nums[maxdq[-1]] <= x:
                maxdq.pop()
            maxdq.append(i - 1)
            while mindq and nums[mindq[-1]] >= x:
                mindq.pop()
            mindq.append(i - 1)
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                if maxdq and maxdq[0] == left:
                    maxdq.popleft()
                if mindq and mindq[0] == left:
                    mindq.popleft()
                left += 1
                
            left_pref = pref[left - 1] if left > 0 else 0
            dp[i] = (pref[i - 1] - left_pref) % MOD
            pref[i] = (pref[i - 1] + dp[i]) % MOD

        return dp[n] % MOD