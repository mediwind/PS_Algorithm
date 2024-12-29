class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for a, b in zip(sorted(s), sorted(t)):
            if a != b:
                return b
        return sorted(t)[-1]