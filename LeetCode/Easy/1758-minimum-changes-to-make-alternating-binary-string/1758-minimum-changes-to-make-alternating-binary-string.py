class Solution:
    def minOperations(self, s: str) -> int:
        cnt, n = 0, len(s)
        for i in range(n):
            cnt += (ord(s[i]) ^ i) & 1
            
        return min(cnt, n - cnt)