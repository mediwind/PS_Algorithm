class Solution:
    def counting(self, mid, piles):
        cnt = 0
        for pile in piles:
            cnt += (pile // mid)
            if pile % mid:
                cnt += 1
        
        return cnt

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lt, rt = 1, max(piles)
        ans = rt
        while lt <= rt:
            mid = (lt + rt) // 2
            res = self.counting(mid, piles)
            if res <= h:
                rt = mid - 1
                ans = min(ans, mid)
            else:
                lt = mid + 1
        
        return ans