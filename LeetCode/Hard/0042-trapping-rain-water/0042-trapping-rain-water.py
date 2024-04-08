class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lt, rt = 0, n - 1
        max_lt, max_rt = height[lt], height[rt]

        answer = 0
        while lt < rt:
            if max_lt <= max_rt:
                lt += 1
                max_lt = max(max_lt, height[lt])
                answer += max_lt - height[lt]
            else:
                rt -= 1
                max_rt = max(max_rt, height[rt])
                answer += max_rt - height[rt]
        
        return answer