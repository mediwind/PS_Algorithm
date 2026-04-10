class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return -1
        
        ans = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    for k in range(j + 1, n):
                        if nums[j] == nums[k]:
                            ans = min(ans, 2 * (k - i))
        
        if ans == float('inf'):
            return -1
        
        return ans