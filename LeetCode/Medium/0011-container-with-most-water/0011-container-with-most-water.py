class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        lt, rt = 0, n - 1
        ans = float('-inf')
        while lt < rt:
            lh, rh = height[lt], height[rt]
            res = (rt - lt) * min(lh, rh)
            ans = max(ans, res)

            if lh < rh:
                lt += 1
            else:
                rt -= 1
        
        return ans