class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        from collections import Counter

        n = len(nums)
        res = []
        for i in range(n - k + 1):
            window = nums[i:i+k]
            cnt = Counter(window)
            items = sorted(cnt.items(), key=lambda iv: (-iv[1], -iv[0]))
            keep = set(v for v,_ in items[:x])
            total = sum(v * cnt[v] for v in keep)
            res.append(total)
            
        return res