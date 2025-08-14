class Solution:
    def largestGoodInteger(self, num: str) -> str:
        candidates = list()
        for i in range(len(num) - 2):
            s = num[i:i+3]
            if s[0] == s[1] == s[2]:
                candidates.append(s)
                
        return max(candidates) if candidates else ""