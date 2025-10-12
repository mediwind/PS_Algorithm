class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        keys = sorted(cnt)
        m = len(keys)
        w = [k * cnt[k] for k in keys]

        dp = [0] * m
        for i in range(m):
            take = w[i]
            j = bisect_right(keys, keys[i] - 3) - 1

            if j >= 0:
                take += dp[j]
                
            notake = dp[i-1] if i > 0 else 0
            dp[i] = max(notake, take)

        return dp[-1] if m > 0 else 0