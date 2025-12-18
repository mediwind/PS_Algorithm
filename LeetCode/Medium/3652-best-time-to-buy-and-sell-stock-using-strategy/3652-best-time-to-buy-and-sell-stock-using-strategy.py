class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2

        base = sum(s * p for s, p in zip(strategy, prices))

        a = [-(s * p) for s, p in zip(strategy, prices)]
        b = [(1 - s) * p for s, p in zip(strategy, prices)]

        pref_a = [0] * (n + 1)
        pref_b = [0] * (n + 1)
        for i in range(n):
            pref_a[i + 1] = pref_a[i] + a[i]
            pref_b[i + 1] = pref_b[i] + b[i]

        max_delta = 0
        for l in range(0, n - k + 1):
            mid = l + half
            r = l + k
            delta = (pref_a[mid] - pref_a[l]) + (pref_b[r] - pref_b[mid])
            if delta > max_delta:
                max_delta = delta

        return base + max_delta