class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dy = dict()

        ans = 0
        for num in arr:
            prev = num - difference
            dy[num] = dy.get(prev, 0) + 1
            ans = max(ans, dy[num])
        
        return ans