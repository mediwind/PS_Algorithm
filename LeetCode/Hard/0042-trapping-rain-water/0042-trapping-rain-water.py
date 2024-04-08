class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]

        maxi = 0
        for i in range(n):
            max_left[i] = maxi
            maxi = max(maxi, height[i])
        
        maxi = 0
        for i in range(n - 1, -1, -1):
            max_right[i] = maxi
            maxi = max(maxi, height[i])
        
        cap = [min(max_left[i], max_right[i]) for i in range(n)]

        answer = 0
        for i in range(n):
            res = cap[i] - height[i]
            if res >= 0:
                answer += res
        
        return answer