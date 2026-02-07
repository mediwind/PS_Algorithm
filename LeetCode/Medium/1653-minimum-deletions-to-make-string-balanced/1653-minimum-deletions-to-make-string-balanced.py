class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans, cnt = 0, 0
        for c in s:
            if c == 'b':
                cnt += 1
            elif cnt:
                ans += 1
                cnt -= 1
        
        return ans