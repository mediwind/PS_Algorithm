class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        ans = [0 for _ in range(n + 1)]
        
        for j in range(m):
            for i in range(n):
                ans[i + 1] = max(ans[i + 1], ans[i]) + mana[j] * skill[i]
            for i in range(n - 1, 0, -1):
                ans[i] = ans[i + 1] - mana[j] * skill[i]
                
        return ans[n]